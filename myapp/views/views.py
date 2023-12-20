from django.shortcuts import render
from django.contrib import messages
from myapp.forms import Registration
import bcrypt
import re
from django.shortcuts import render,redirect,get_object_or_404
import json
from django.http import HttpResponse,JsonResponse
from ..models import Customer,Product,Payment,Cart,Order,BlogPost,Blog_comment,Contact_message
from django.utils.safestring import mark_safe
from .emailview import activate,activate_email,mailtest,forgotPassword
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
from django.contrib import messages
#from myapp.Doctor_handwritten_prescription.src.predict import main
from subprocess import run
import os
import re
import random
from django.db import transaction
import datetime
from django.db.models import Q



# Create your views here.
def checkout(request):
    return render(request,"checkout.html")   

def home(request):
    try:
        user_credential = request.session.get('user_credential')
        user = Customer.objects.get(Customer_Email=user_credential)
    
        context ={
        'user_credentials':user_credential,
        'users':user
        }   
        return render(request,"home.html",context)
    except Customer.DoesNotExist:
        return render(request,"home.html")
    
#def products(request):
    #return render(request,"products.html")

def homes(request, login_status):
    return render(request,"home.html", {'login_status':login_status})

def prescription_approval(request):
    return render(request,"prescription_approval.html")

def blog(request):
    try:
        blog_content = BlogPost.objects.all()
        user_credential = request.session.get('user_credential')
        user = Customer.objects.get(Customer_Email=user_credential)
        context = {
            'blog_contents':blog_content,
            'user_credentials': user_credential,
            'users':user,
            
        }
        return render(request,"blog.html",context)
    except:
        blog_content = BlogPost.objects.all()
        context = {
            'blog_contents':blog_content,
            
        }
        return render(request,"blog.html",context)
    
def blog_details(request,id):
    try:
        user_credential = request.session.get('user_credential')
        user = Customer.objects.get(Customer_Email=user_credential)
        user_auth = request.session.get('user_credential')
        blog_piece = BlogPost.objects.get(id=id) # id is id of blog content
        blog_comment = Blog_comment.objects.filter(blog_id_id=id)# id is id of blog content
        comment_count = blog_comment.count()
        comment_greater_than_1 = None
        if comment_count>1:
            comment_greater_than_1 = True
        else:
            comment_greater_than_1 = False
        context ={
            'blog_piece':blog_piece,
            'blog_comments':blog_comment,
            'comment_count':comment_count,
            'comment_greater_than_1':comment_greater_than_1,
            'user_auth': user_auth,
            'user_credentials':user_credential,
            'users':user,
        }
        return render(request,'blog_details.html',context)
    except:
        blog_piece = BlogPost.objects.get(id=id) # id is id of blog content
        blog_comment = Blog_comment.objects.filter(blog_id_id=id)# id is id of blog content
        comment_count = blog_comment.count()
        comment_greater_than_1 = None
        if comment_count>1:
            comment_greater_than_1 = True
        else:
            comment_greater_than_1 = False
        context ={
            'blog_piece':blog_piece,
            'blog_comments':blog_comment,
            'comment_count':comment_count,
            'comment_greater_than_1':comment_greater_than_1,
            
        }
        return render(request,'blog_details.html',context)
#def profile(request):
    #return render(request,"profile.html")
    
def blog_comment(request):
    blog_id = request.POST['blog_id']
    #user_id = 
    
    comment = request.POST['comment']
    blog_id = request.POST['blog_id']
    user_id = request.session.get('user_id')
    name = Customer.objects.get(Customer_ID=user_id).Customer_Name        
    comment_date = datetime.datetime.today().now()

    comments_save =  Blog_comment(user_id=user_id,user_name=name,comment=comment,comment_date=comment_date,blog_id_id = blog_id)
    comments_save.save()
    return redirect('blog_details',blog_id)
    
    messages.error(request,'Please login to account to comment')
    
    return redirect('blog_details',blog_id)

def delete_comment(request,comment_id,blog_id):
    comment_to_delete = Blog_comment.objects.get(id=comment_id)
    comment_to_delete.delete()
    blog_redirect = blog_id
    return redirect('blog_details',blog_redirect)




def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def terms(request):
    return render(request,"terms.html")

def contact(request):
    return render(request,"contact.html")

def forgot(request):
    return render(request,"forgot.html")

def activateEmailMessage(request):
    user = request.POST.get('name')
    email = request.POST.get('email')
    success_message = mark_safe(
        f'Dear <b>{user}</b>, Please check your email <b>{email}</b> inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )

    messages.success(request, success_message)

def insertuser(request):
    if request.method == 'POST':
        
        Regform = Registration(request.POST)
        
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['DOB']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        gender = request.POST['gender']
        password = request.POST['tp_password']
        c_password = request.POST['tp_con_password']
        
            


        if request.POST.get('name') == "":
            return render(request,"register.html",{'error_name':True})
        
        
        if request.POST.get('email') == "":
            return render(request,"register.html",{'error_email':True})
        
        
        if request.POST.get('DOB') == "":
            messages.error(request, 'Add Date of birth')
            return redirect('registration')
            #return render(request,"register.html",{'error_DOB':True})  
        
        if request.POST.get('phone_number') == "":
            messages.error(request, 'Add Phone Number')
            return redirect('registration')
            #return render(request,"register.html",{'phone_number':True})  
        
        if request.POST.get('address') == "":
            messages.error(request, 'Add Permanent Address')
            return redirect('registration')
            #return render(request,"register.html",{'address':True}) 
        
        if request.POST.get('gender') == "":
            messages.error(request, 'Add Gender')
            return redirect('registration')
            #return render(request,"register.html",{'gender':True}) 
        
        if request.POST.get('tp_password') == "":
            return render(request,"register.html",{'error_password':True})
        
        #email validation
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email = request.POST['email']
        if not re.search(pattern,email):
            return render(request,"register.html",{'error_email_valid':True})
            #checking if email is already registered
        desired_value = email  # Replace this with the value you want to check.
        value_exists = Customer.objects.filter(Customer_Email=desired_value).exists()
        if value_exists:
            messages.error(request, "Email is already registered! Try New Email.")
            return render(request,"register.html")
        
         # Checking password matches confirm passowrd
        password = request.POST['tp_password']
        c_password = request.POST['tp_con_password']
        if password != c_password:
            messages.error(request, "Password and Confirm Password do not match.")
            return render(request,"register.html",{'error_email_valid':True})  # Redirect to the registration page if passwords don't match

        if len(password)<3:
            return render(request,"register.html",{'error_password_num':True})
        

       #password validation
        pattern = r'^(?=.*[a-z])(?=.*[A-Z]).+$'
        password = request.POST['tp_password']
        if not re.search(pattern, password):
            return render(request,"register.html",{'password_char':True})
        
        
        request.session['email'] = email
        
        hashed_password = make_password(password)
        c_hashed_password = make_password(c_password)

        activate_email(request)
        
        us = Customer(Customer_Name = name, Customer_Email=email, Customer_Password=hashed_password, Customer_Confirm_Password=c_hashed_password, account_status='inactive', address=address, dob=dob, gender=gender, phone_number=phone_number, role='', user_image='' )
        us.save()
        return redirect('registration')
        
        
def login_user(request):
    if request.method == 'POST':
        emails = request.POST['email']
        password = request.POST['tp_password']
        request.session['email'] = emails

        try:
            user_id = Customer.objects.get(Customer_Email=emails).Customer_ID
            user = Customer.objects.get(Customer_Email=emails)
            
            if check_password(password, user.Customer_Password ):
                
                mailtest(request)  # Redirect to the home page after successful login
                request.session['user_credential'] = emails
                request.session['user_id'] = user_id
                return render(request,'2-FA.html')
            else:
                # Incorrect password
                messages.error(request, 'Invalid Email or Password.')
        except Customer.DoesNotExist:
            # User not found
            messages.error(request, 'Invalid Email or Password.')

    return render(request, 'login.html')  # Replace 'login.html' with your login template file path

def resend_code(request):
    mailtest(request)
    return redirect('verify')

def profile(request):

    
        user = request.session.get('user_credential')
        order = Order.objects.filter(email=user)
        customer = get_object_or_404(Customer, Customer_Email=user)
        context={
            'credentials':customer,
            'users':user,
            'orders':order,
        }
        return render(request,'profile.html',context)
    
        return HttpResponse('Invalid request. Please login to the account')

def update_profile(request):
    if request.method == "POST":

        user_id = request.session.get('user_credential')
        user = Customer.objects.get(Customer_Email=user_id)

        user_name = request.POST['user_name']
        user_dob = request.POST['dob']
        user_email = request.POST['user_email']
        user_number = request.POST['user_number']
        user_gender = request.POST['user_gender']
        user_address = request.POST['user_address']

        user.Customer_Name = user_name
        user.Customer_Email = user_email
        user.dob = user_dob
        user.phone_number = user_number
        user.gender = user_gender
        user.address = user_address
        user.save()
        return redirect('profile.html')

def new_password(request):
    user_session = request.session.get('user_credential')
    user = Customer.objects.get(Customer_Email=user_session)
    real_pass = user.Customer_Password

    
    old_pass = request.POST['old_pass']
    new_pass = request.POST['new_pass']
    con_new_pass = request.POST['con_new_pass']
    if not check_password(old_pass,real_pass):
        messages.error(request,'Incorrect Password')
        return redirect('profile.html')

    if con_new_pass != new_pass:
        messages.error(request,'Password do not match')
        return redirect('profile.html')
    else:
        user.Customer_Password = make_password(new_pass)
        user.Customer_Confirm_Password = make_password(con_new_pass)
        user.save()
        messages.success(request,'Password Changed')
        return redirect('profile.html')

def reset_password(request):
    emails = request.POST.get('email')

    try:
        user = Customer.objects.get(Customer_Email=emails)
        
        if user:
            
            forgotPassword(request)  # Redirect to the home page after successful login
            
        else:
            # Incorrect password
            messages.error(request, 'Invalid Email.')
    except Customer.DoesNotExist:
            messages.error(request, 'Email does not exist.')
    return render(request,'forgot.html')

def profile_image(request):
    user = request.session.get('user_credential')
    image = request.FILES['user_image']

    user_image = Customer.objects.get(Customer_Email = user)
    user_image.user_image = image
    user_image.save()
    return redirect('profile.html')

def update_password(request):
    change_password = request.POST['change_password']
    change_ConfirmPassword = request.POST['change_confirmPassword']
    email = request.session.get('email')

    try:
        user_to_update = Customer.objects.get(Customer_Email=email)
        user_to_update.Customer_Password = make_password(change_password)
        user_to_update.Customer_Confirm_Password = make_password(change_ConfirmPassword)
        user_to_update.save()
    except Customer.DoesNotExist:
        messages.error("error")
    return render(request,'login.html',{'email_check':email})

def contact_message(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone_number']
    subject = request.POST['msg_subject']
    message = request.POST['message']

    contact_message = Contact_message(name=name,email=email,phone=phone,subject=subject,message=message,message_posted=datetime.date.today())
    contact_message.save()
    messages.success(request,'Thank you for sending message, we will soon respond to your feedback.')
    return redirect('contact')


def dashboard(request):
    return  render(request,"backend/index.html")
    
def sales_dashboard(request):
    return render(request,"backend/dashboards/sales.html")

#analytics dashboards
def analytics_dashboard(request):
    return render(request,"backend/dashboards/analytics.html")

#ecommerce dashboards
def ecommerce(request):
    return render(request,"backend/dashboards/ecommerce.html")
    


def predict_view(request,id):
    
    global uploaded_image
    uploaded_image = request.FILES.get('images')
    if uploaded_image:
            # Define the path where you want to save the image in the 'media' folder
            media_folder = 'media/'
            image_path = os.path.join(media_folder, uploaded_image.name)

            # Open the image file and save it
            with open(image_path, 'wb') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

            # Now, you can use 'image_path' for further processing or pass it to your prediction function
            #result = predict_image(image_path)
    return HttpResponse(predict_image(request,uploaded_image,id))
    


def predict_image(request,param,id):

    #json_data = list_cards
    image_path = os.path.abspath(os.path.join('media'))

    # Then, append the file name to it
    checkpoint_file_path = os.path.join(image_path,str(param))

     # Define the command to run the script with appropriate arguments
    
    #command = ["python", "myapp/Doctor_handwritten_prescription/predict.py", "path/to/your/image.png"]
    command = ["python", "myapp/Doctor_handwritten_prescription/src/predict.py", checkpoint_file_path]

    # Run the script using subprocess
    result = run(command, capture_output=True, text=True)
    
    # Process the output and send it to the template
    output = result.stdout
    
    #return uploaded_image.name
# Find the starting index of the "Prediction --->" substring
    start_index = output.find("Prediction --->")

# Check if the "Prediction --->" substring is found in the output
    if start_index != -1:
    # Extract the prediction portion after "Prediction --->"
        prediction_start = start_index + len("Prediction --->")
        prediction = output[prediction_start:].strip()
        # Define a regular expression pattern to match text inside square brackets
        pattern = r'\[\[(.*?)\]\]'

        # Use re.sub to replace the matched pattern with an empty string
        prediction_modify = re.sub(pattern, '', prediction).strip()
        # Specify the 'id' you want to find
        desired_id = id

        # Initialize a variable to store the result
        result_dict = None
        #list_cards[id]['status'] = None
        # Iterate through the list to find the dictionary with the desired 'id'
        for card in list_cards:
            if card.get('id') == desired_id:
                #card['status'] = 'empty'
                result_dict = card
                break  # Stop the loop once the desired 'id' is found
      
        image_name_with_extension = uploaded_image.name
        image_name_without_extension = os.path.splitext(image_name_with_extension)[0]
        
        if prediction_modify.lower() == result_dict['name'].lower():
            result_dict['status'] = 'matched'
            if 'id' in result_dict:
                product_id = result_dict['id']
                for card in list_cards:
                    if card.get('id') == product_id:
                        card['status'] = 'matched'
        elif prediction_modify.lower() != result_dict['name'].lower():
            result_dict['status'] = 'not_matched'
            if 'id' in result_dict:
                product_id = result_dict['id']
                for card in list_cards:
                    if card.get('id') == product_id:
                        card['status'] = 'not_matched'
        else:
            if 'id' in result_dict:
                product_id = result_dict['id']
                for card in list_cards:
                    if card.get('id') == product_id:
                        card['status'] = None
    
        result_dict

       
        
        

        def check_status_condition(list_cards):
            if not list_cards:
                return None  # Return None for an empty list.

            # Check if any card has no 'status' key or has 'not_matched' status.
            has_not_matched = any('status' not in product or product['status'] == 'not_matched' for product in list_cards)

            # If no card has 'not_matched' status, return True; otherwise, return False.
            return not has_not_matched
            
            

        # Assuming list_cards is defined elsewhere in your code

        status_condition_met = check_status_condition(list_cards)

        
        context = {
            'list_cards':list_cards,
            'approv_valid':status_condition_met,
            'total': total
            
        }
        #context.append(list_cards.get('name').lower())
        return render(request, 'prescription_approval.html',context)
        #return HttpResponse(list_cards)    
    return  HttpResponse('')



#view for cart 

def Products(request):
    
    try:
        user_credential = request.session.get('user_credential')
        user = Customer.objects.get(Customer_Email=user_credential)
        
        #products = list(Product.objects.values())
        products = list(Product.objects.values())
        product_image = Product.objects.all()
        total_prod = Product.objects.all().count()
        cartItem = list(Product.objects.values('id','name','image','price'))
        context = {
                'products': products,
                'product_image': product_image,
                'total_prod': total_prod,
                'cartItem':cartItem,
                'user_credentials':user_credential,
                'users':user
            }
        return render(request,"products.html",context)
    except Customer.DoesNotExist:
        products = list(Product.objects.values())
        product_image = Product.objects.all()
        total_prod = Product.objects.all().count()
        cartItem = list(Product.objects.values('id','name','image','price'))
        context = {
                'products': products,
                'product_image': product_image,
                'total_prod': total_prod,
                'cartItem':cartItem,
                
            }
        return render(request,"products.html",context)

def order_process(request):
    json_data = list_cards
    if request.POST['transaction_id'] == "":
        messages.error(request,'Please Add Transaction ID')
        return redirect('checkout.html')
    
        
    if request.POST['phone_number'] == "":
        messages.error(request,'Add Phone Number')
        return redirect('checkout.html')
    if request.method == 'POST':
        try:
            # Iterate through the JSON data, where each item contains 'id' and 'quantity'
            for item in json_data:
                product_id = item.get('id')
                selected_quantity = item.get('quantity')

                # Retrieve the product from the database by ID
                product = Product.objects.get(pk=product_id)

                # Check if there are enough products in stock
                if product.quantity >= selected_quantity:
                    # Subtract the selected quantity from the database
                    product.quantity -= selected_quantity
                    product.save()
                else:
                    return JsonResponse({'message': 'Not enough products in Stock.'}, status=400)

            #return JsonResponse({'message': 'Quantity subtracted successfully.'}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product not found.'}, status=404)

            return JsonResponse({'message': 'Invalid request method.'}, status=405)
    
    
    payment_process(request)
    messages.success(request,'Payment Successful! Your Order is waiting for approval')
    return redirect('profile.html')

def process_cart(request,order_id):
   
    # Get the JSON data from the request.
    #json_data = request.POST.get("cart_data")
    
    #cart_session = random.randint(1000,9999)
    email = request.session.get('user_credential') # Get the currently logged-in user.
    #request.session['cart_session'] = cart_session
    # Loop through the cart items and create CartItem objects.
 
        
    with transaction.atomic():
        json_data = cart_list
        for item in json_data:
            item_name = item["name"]
            item_price = item["price"]
            

            # Create a new CartItem record for the user.
            Cart.objects.create(
                email=email,
                item_name=item_name,
                item_price=item_price,
                total=total,
                cart_session = None,
                order_id = order_id
            )

            
        # Redirect to a confirmation page or perform any additional actions.
        return HttpResponse(email)
        return redirect("profile")
  
    


def payment_process(request):
    email = request.session.get('user_credential')
    transaction_number = request.POST['transaction_id']
    user_name = Customer.objects.get(Customer_Email=email).Customer_Name
    cart_total = total
    phone_number = request.POST['phone_number']
    gateway = request.POST['gateway']
    #return HttpResponse(cart_total)
    order_id = random.randint(1,9999)
    order = Order(order_id=order_id,order_date=datetime.date.today(),customer_name=user_name,email=email,status='pending',total=cart_total,gateway=gateway)
    order.save()
    

    payment = Payment(transaction_number = transaction_number,phone_number = phone_number, email = email,order_id=order)
    payment.save()

    process_cart(request,order)    

def checkout(request):
    if 'user_credential' in request.session:
        user_email = request.session['user_credential']
        try:
            user = Customer.objects.get(Customer_Email=user_email)  # Get user by email
        except Customer.DoesNotExist:
            # Handle the case where the user does not exist
            user = None
    else:
        # Handle the case where 'user_credential' is not in the session
        user = None

    product_database = Product.objects.all()

    
    cart_data = request.POST.get('listCardsData', '')
        #global totals # declared global only for particular views to access it
        #totals = request.POST.get('total')
    try:
        global cart_list # declared global only for particular views to access it
        cart_list = json.loads(list_cards_data)
    except json.JSONDecodeError:
            # Handle the case where JSON decoding fails
            cart_list = []


    contexts = {
        'cart_list': cart_list,
        'product_database': product_database,
        'user': user,
        'total': total
    }
    return render(request, 'checkout.html', contexts)

def prescription_approval(request):
    #if request.method == 'POST':
        global  list_cards_data 
        list_cards_data = request.POST.get('listCardsData')
        #cart total
        global total 
        total = request.POST.get('total')
        # Convert the JSON data back to a Python object
        global list_cards
        list_cards = json.loads(list_cards_data)

        # Initialize an empty list to store the dictionaries
        list_of_dicts = []

# Check if 'list_cards' is a list (to handle dynamic input)
        if isinstance(list_cards, list):
            # Iterate through each dictionary and add it to 'list_of_dicts'
            for card in list_cards:
                list_of_dicts.append(card)
        
        # contexts
        contexts = {
            'list_cards':list_cards,
            'total':total,
            'list_of_dicts':list_of_dicts,
        }
        
        #return JsonResponse(list_of_dicts ,safe=False)
        #return HttpResponse(list_of_dicts)
        return render(request,"prescription_approval.html",contexts)
    #else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
def delete_sessions(request, session_keys):
    for key in session_keys:
        if key in request.session:
            del request.session[key]

    # You can optionally return a response or redirect to a specific page
    return HttpResponse('')

def logout(request):
    # List of session keys to delete
    session_keys_to_delete = ['login_status', 'user_credential','user_id']

    # Call the delete_sessions function to delete the specified keys
    delete_sessions(request, session_keys_to_delete)

    # Continue with your view logic
    # ...
    return redirect('login.html')
