/*code for cart functionality*/
let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let card = document.querySelector('.active')
let list = document.querySelector('.list');
let listCard = document.querySelector('.listCard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');




openShopping.addEventListener("click", () => {
    // Toggle the visibility of the cart element by changing its style.display property
    if (card.style.display === "none" || card.style.display === "") {
        cart.style.display = "block"; // Show the cart
    } else {
        card.style.display = "none"; // Hide the cart
    }
});



openShopping.addEventListener('click', () => {
    body.classList.add('active');

})



closeShopping.addEventListener('click', () => {
    body.classList.remove('active');
})



//textcontent of JSON
let cartItem_jsondata = JSON.parse(document.getElementById('cartItem').textContent) //list of cart items

let cartItem = cartItem_jsondata


let jsondata = JSON.parse(document.getElementById('product-list').textContent) //information of all products
let jsonImageData = jsondata["image"]

let prodIdElement = document.getElementById('prod_id');
let prodNameElement = document.getElementById('prod_title');
let prodPriceElement = document.getElementById('prod_price');
let imageSource = document.getElementById('prod_img')


/*let product = [
 {
  id: prodIdElement.textContent,
  name: prodNameElement.textContent,
  price: prodPriceElement.textContent,
  image: imageSource.getAttribute('src')
 }

]*/



let product = jsondata

let listCards = []; // list of item and their quantity in cart
function initApp() {




    product.forEach((value, key) => {
            let newDiv = document.createElement('div');
            newDiv.classList.add('item');
            newDiv.innerHTML = `
            <img src="/media/${value.image}" >
            <div class="title">${value.name}</div>
            <div class="description">${value.description}</div>
            <div class="price"><span>$</span>${value.price}</div>
            <div class="quantity">${value.quantity}</div><span>pcs</span>
            
            <br><br>
            `;
            if (value.quantity > 0) {
                newDiv.innerHTML += `<button onclick="addToCart(${key})">Add To Cart</button>`;
            } else {
                newDiv.innerHTML += `<div style ="color:red" class="title"><b>Out of Stock</b></div>`
            }
            list.appendChild(newDiv);

            //if()

            /*var image = document.getElementById('prod_id').getAttribute('src');

            var title = document.getElementById('prod_title');
            value.name = title.innerText
            var price = document.getElementById('prod_price');
            value.price = price.innerText*/


        })
        //if()
}

initApp();

function addToCart(key) {
    if (listCards[key] == null) {
        // copy product form list to list card
        listCards[key] = JSON.parse(JSON.stringify(cartItem[key]));


        listCards[key].quantity = 1;
        //let test = 0;
        prepareAndSubmitListCardsData(listCards[key])
        document.getElementById('cartbtn').style.display = 'block'
    }

    reloadCard();

}

function reloadCard(item) {
    listCard.innerHTML = '';
    let count = 0;
    let totalPrice = 0;
    listCards.forEach((value, key) => {
        totalPrice = totalPrice + value.price;
        count = count + value.quantity;
        if (value != null) {
            let newDiv = document.createElement('li');
            newDiv.innerHTML = `
                <div><img src="/media/${value.image}"/></div>
                <div>${value.name}</div>
                <div>${value.price.toLocaleString()}</div>
                <div>
                    <button onclick="changeQuantity(${key}, ${value.quantity - 1})">-</button>
                    <div class="count">${value.quantity}</div>
                    <button onclick="changeQuantity(${key}, ${value.quantity + 1})">+</button>
                </div>`;
            listCard.appendChild(newDiv);

        }


    })


    //prepareAndSubmitListCardsData(listCards[key])
    total.innerText = totalPrice.toLocaleString();
    quantity.innerText = count;
    document.getElementById('total').value = totalPrice.toLocaleString()
}

function changeQuantity(key, quantity) {
    if (quantity == 0) {
        delete listCards[key];
        delete prepareAndSubmitListCardsData(listCards[key])
        document.getElementById('cartbtn').style.display = 'none'
            //


    } else {
        listCards[key].quantity = quantity;
        listCards[key].price = quantity * product[key].price;
        document.getElementById('cartbtn').style.display = 'block'
        if (quantity > product[key].quantity) {
            alert('insufficient quantity')
            document.getElementById('cartbtn').style.display = 'none'
        }
    }


    reloadCard();
    prepareAndSubmitListCardsData(listCards);
}

/*function prepareAndSubmitListCardsData(cartItem) {
  // Assuming listCards is your JavaScript object containing cart data
  let listCardsData = JSON.stringify(listCards);
  let filteredArray = listCardsData.filter(element => element !== null);
  //cartItem = listCardsData
  //JSON.stringify(cartItem)
  //items = [cartItem]
  document.getElementById('listCardsData').value = filteredArray ;
  
}*/

/*function prepareAndSubmitListCardsData(cartItem) {
  // Assuming listCards is your JavaScript object containing cart data
  let filteredArray = Object.keys(listCards).reduce((result, key) => {
    if (listCards[key] !== null) {
      result[key] = listCards[key];
    }
    return result;
  }, []);

  document.getElementById('listCardsData').value = JSON.stringify(filteredArray);
}*/
function prepareAndSubmitListCardsData() {
    // Assuming listCards is your JavaScript object containing cart data
    let filteredArray = Object.keys(listCards).reduce((result, key) => {
        if (listCards[key] !== null) {
            result[key] = listCards[key];
        }
        return result;
    }, {});

    // Convert the filtered object into an array of its values
    let filteredArrayValues = Object.values(filteredArray);

    document.getElementById('listCardsData').value = JSON.stringify(filteredArrayValues);
    //getCartItem(JSON.stringify(filteredArrayValues))
    let cartItem = JSON.stringify(filteredArrayValues)
    return cartItem

}







// disabling input fields

// Function to disable the input element


document.addEventListener("DOMContentLoaded", function() {
    var input = document.getElementById("total");
    input.addEventListener("input", function() {
        // Reset the input value if it's changed by the user
        input.value = "This input is disabled";
    });

    var input2 = document.getElementById("listCardsData");
    input2.addEventListener("input", function() {
        // Reset the input value if it's changed by the user
        input2.value = "This input is disabled";
    });
});


// Function to display products based on the search query
function displayProducts(query) {
    const productDisplay = document.querySelector('.list');
    productDisplay.innerHTML = ''; // Clear the display

    product.forEach((matchingProduct, key) => {
        if (matchingProduct.name.toLowerCase().includes(query.toLowerCase()) || query === '') {
            let newDiv = document.createElement('div');
            newDiv.classList.add('item');
            newDiv.innerHTML = `
                <img width="50px" height="50px" src="/media/${matchingProduct.image}">
                <div class="title">${matchingProduct.name}</div>
                <div class="price"><span>$</span>${matchingProduct.price}</div>
                <div class="quantity">${matchingProduct.quantity}<span>pcs</span></div>
                <br><br>
            `;
            if (matchingProduct.quantity > 0) {
                newDiv.innerHTML += `<button onclick="addToCart(${key})">Add To Cart</button>`;
            } else {
                newDiv.innerHTML += `<div style="color: red" class="title"><b>Out of stock</b></div>`;
            }
            productDisplay.appendChild(newDiv);
        }
    });
}

// Event listener for the search input
const searchInput = document.getElementById('search-input');
searchInput.addEventListener('input', function() {
    const query = searchInput.value;
    displayProducts(query);
});