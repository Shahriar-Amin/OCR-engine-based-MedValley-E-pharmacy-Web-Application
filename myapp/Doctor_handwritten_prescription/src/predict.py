"""
Usage: predict.py [-m MODEL] [-s BS] [-d DECODE] [-b BEAM] [IMAGE ...]

-h, --help    show this
-m MODEL     model file [default: ./checkpoints/crnn_synth90k.pt]
-s BS       batch size [default: 256]
-d DECODE    decode method (greedy, beam_search or prefix_beam_search) [default: beam_search]
-b BEAM   beam size [default: 10]

type python predict.py image directory in cmd to run the file and see results

E.g. python predict.py ../data/cropped_sample/writing/Seclo.png
"""

from docopt import docopt
import torch
from tqdm import tqdm
from torch.utils.data import DataLoader
import os
import sys



#from .config import common_config as config
#from .config import common_config as config
from config import common_config as config


from drugs import findDrug
from dataset import Synth90kDataset, synth90k_collate_fn
from model import CRNN
from evaluate import evaluate
from ctc_decoder import ctc_decode


def predict(crnn, dataloader, label2char, decode_method, beam_size):
    crnn.eval()
    pbar = tqdm(total=len(dataloader), desc="Predict")

    all_preds = []
    with torch.no_grad():
        for data in dataloader:
            device = 'cuda' if next(crnn.parameters()).is_cuda else 'cpu'

            images = data.to(device)

            logits = crnn(images)
            log_probs = torch.nn.functional.log_softmax(logits, dim=2)

            preds = ctc_decode(log_probs, method=decode_method, beam_size=beam_size,
                               label2char=label2char)
            all_preds += preds

            pbar.update(1)
        pbar.close()

    return all_preds

#absolute file path
checkpoints_dir = os.path.abspath(os.path.join( 'myapp/Doctor_handwritten_prescription', 'checkpoints'))

# Then, append the file name to it
checkpoint_file_path = os.path.join(checkpoints_dir, 'crnn_synth90k.pt')

def show_result(paths, preds):
    print('\n===== Result =====')
    for path, pred in zip(paths, preds):
        texts = ''.join(pred)
        result = findDrug(texts)
        print(f'Prediction ---> {result}')


def main():
    arguments = docopt(__doc__)

    images = arguments['IMAGE']
    # images = crop(image)
    #reload_checkpoint = arguments['-m']
    #reload_checkpoint = '../checkpoints/crnn_synth90k.pt'
    reload_checkpoint = checkpoint_file_path
    batch_size = int(arguments['-s'])
    decode_method = arguments['-d']
    beam_size = int(arguments['-b'])

    img_height = config['img_height']
    img_width = config['img_width']

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'device: {device}')

    predict_dataset = Synth90kDataset(paths=images,
        img_height=img_height, img_width=img_width)

    predict_loader = DataLoader(
        dataset=predict_dataset,
        batch_size=batch_size,
        shuffle=False)

    num_class = len(Synth90kDataset.LABEL2CHAR) + 1
    crnn = CRNN(1, img_height, img_width, num_class,
                map_to_seq_hidden=config['map_to_seq_hidden'],
                rnn_hidden=config['rnn_hidden'],
                leaky_relu=config['leaky_relu'])
    crnn.load_state_dict(torch.load(reload_checkpoint, map_location=device))
    crnn.to(device)

    preds = predict(crnn, predict_loader, Synth90kDataset.LABEL2CHAR,
                    decode_method=decode_method,
                    beam_size=beam_size)

    
    show_result(images, preds)
    print(preds)
    return preds

if __name__ == '__main__':
    main()
