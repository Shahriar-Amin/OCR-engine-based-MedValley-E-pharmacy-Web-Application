from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpRequest
from ..models import Product, Contact_message, BlogPost, Customer, Order, Cart, Invoice, Admin, Payment
from datetime import datetime
import datetime
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import string
import random
from django.db import models


def blog_list(request):
    return render(request,"backend/pages/blog/blog_list.html")

def blog_post(request):
    return render(request,"backend/pages/blog/post.html")

def blog_list(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,"backend/pages/blog/blog_list.html",context)

def blog_publish(request):
    if request.method == 'POST':

        blog_title =   request.POST['blog_title']    
        author_name = request.POST['author_name']
        blog_date = datetime.datetime.today().date()
        writing = request.POST['writing']
        blog_image = request.FILES['blog_image']
        blog_data = [blog_title,author_name,writing,blog_image,blog_date]
        if None in blog_data:
            messages.error(request,'Please enter all of the data')
        else:

            blog = BlogPost(author_name=author_name,blog_title=blog_title,user_image=blog_image,writing=writing,date=blog_date)
            blog.save()
            #messages.success(request,'Blog published')

    return redirect('blog_post')

def blog_edit(request,id):
    blog = BlogPost.objects.get(id=id)
    context = {
        'blogs':blog
    }
    return render(request,'backend/pages/blog/blog_edit.html',context)

def blog_delete(request,id):
    blog_delete = BlogPost.objects.get(id=id)
    blog_delete.delete()
    return redirect('blog_list')

def update_blog(request,id):
    blog_to_update = BlogPost.objects.get(id=id)
    blog_to_update.writing = request.POST['blog_writing']
    blog_to_update.blog_title = request.POST['blog_title']
    blog_to_update.save()
    return redirect('blog_list')

#mesage view


def compose(request):
    return render(request,"backend/apps/inbox/compose.html")

def reply(request):
    return render(request,"backend/apps/inbox/reply.html")

#chat view
def chat_drawer(request):
    return render(request,"backend/apps/chat/drawer.html")

def group_chat(request):
    return render(request,"backend/apps/chat/group.html")

def private_chat(request):
    return render(request,"backend/apps/chat/private.html")

#invoice
def invoice(request):
    return render(request,"backend/apps/invoice/invoice.html")

def invoice2(request):
    return render(request,"backend/apps/invoices/view/invoice-2.html")

def invoice3(request):
    return render(request,"backend/apps/invoice/view/invoice-3.html")

def create_invoice(request):
    return render(request,"backend/apps/invoice/create.html")


#customers view

def customer(request):
    return render(request,"backend/apps/customers/getting-started.html")

def account_deactivate(request,id):
    
    user_account = Customer.objects.get(Customer_ID=id)
    user_account.account_status = 'inactive'
    subject = 'Account deactivation'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_account.Customer_Email]
    name = user_account.Customer_Name
    context={
        'name':name
    }
    html_content = render_to_string('account-message.html',context)
    
    msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    #return HttpResponse(user_id.account_status)
    user_account.save()
    return redirect('customer_list')

def customer_delete(request,id):
    customer_delete = Customer.objects.filter(Customer_ID=id)
    customer_delete.delete()
    return redirect('customer_list')

def account_activate(request,id):
    
    user_account = Customer.objects.get(Customer_ID=id)
    user_account.account_status = 'active'
    
    
    #return HttpResponse(user_id.account_status)
    user_account.save()
    return redirect('customer_list')

def customer_list(request):
    customer_list = Customer.objects.all()
    context = {
        'customers':customer_list
    }
    return render(request,"backend/apps/ecommerce/customers/listing.html",context)
    return render(request,"backend/apps/ecommerce/customers/listing.html")

def customer_view(request):
    return render(request,"backend/apps/customers/view.html")

def customer_edit(request,id):
    customer = Customer.objects.get(Customer_ID=id)
    return render(request,"backend/apps/ecommerce/customers/customer_edit.html",{'customer':customer})

def customer_update(request,id):
    customer_to_update = Customer.objects.get(Customer_ID=id)
    customer_to_update.Customer_Name = request.POST['name']
    customer_to_update.email = request.POST['email']
    customer_to_update.address = request.POST['address']

    customer_to_update.save()
    return redirect('customer_list')

# contact views

def contact(request):
    return render(request,"backend/apps/contacts/getting-started.html")

def add_contact(request):
    return  render(request,"backend/apps/contacts/add-contact.html")

def edit_contact(request):
    return render(request,"backend/apps/contacts/edit-contact.html")

def view_contact(request):
    return render(request,"backend/apps/contacts/view-contact.html")

#file manager


def files(request):
    return render(request,"backend/apps/file-manager/files.html")

def folders(request):
    return render(request,"backend/apps/file-manager/folders.html")

def root_directory(request):
    return render(request,"backend/apps/file-manager/.html")

def admin_logout(request):
    del request.session['admin_login']
    return redirect('sign_in')

#user management

def user_list(request):
    return render(request,"backend/apps/user-management/users/list.html")

def user_view(request):
    return render(request,"backend/apps/user-management/users/view.html")

def permissions(request):
    return render(request,"backend/apps/user-management/permissions.html")

def role_list(request):
    return render(request,"backend/apps/user-management/roles/list.html")

def role_view(request):
    return render(request,"backend/apps/user-management/roles/view.html")

#authentication views

def two_factor(request):
    return render(request,"backend/authentication/general(2)/two-factor.html")

def sign_up(request):
     # Create an instance of HttpRequest
    request = HttpRequest()

# Set the request method (GET, POST, etc.)
    request.method = 'GET'

# Set the request path
    request.path = 'backend/authentication/general(2)/sign-up.html'
    response= render(request,"backend/authentication/general(2)/sign-up.html")
    return response

def sign_in(request):
    # Create an instance of HttpRequest
    return render(request,"backend/authentication/general(2)/sign-in.html")



def reset_password(request):
    return render(request,"backend/authentication/general(2)/reset-password.html"),

def customer_message(request):
    contact_message = Contact_message.objects.all()
    context = {
        'contact_messages':contact_message
    }
    return render(request,'backend/contact_message.html',context)

def verify_email(request):
    return render(request,"backend/authentication/general/verify-email.html"),

def welcome_user(request):
    return render(request,"backend/authentication/general/welcome.html"),

#ecommerce views

#catalog views

def add_category(request):
    return render(request,"backend/apps/ecommerce/catalog/add-category.html"),

def new_products(request):
       return render(request,"backend/apps/ecommerce/catalog/add-product.html")

def categogries(request):
    return render(request,"backend/apps/ecommerce/catalog/categories.html"),

def edit_categories(request):
    return render(request,"backend/apps/ecommerce/catalog/edit-category.html"),

def product_edit(request):
    return render(request,"backend/apps/ecommerce/catalog/edit-product.html")

def product_editing(request,id):

    product_to_edit = Product.objects.get(id=id)
    

    context={
        'edit':product_to_edit
    }

    return render(request,"backend/apps/ecommerce/catalog/edit-product.html",context)

def product_update(request,id):

    product_to_update = Product.objects.get(id=id)

    product_to_update.name = request.POST['product_name']
    product_to_update.description = request.POST['description']
    product_to_update.price = request.POST['price']
    product_to_update.quantity = request.POST['quantity']
    product_to_update.save()

    return redirect('products_list')

def delete_products(request,id):

    delete_products = Product.objects.get(id=id)
    delete_products.delete()
    return redirect('products_list')

def products(request):
    products = Product.objects.all()

    return render(request,"backend/apps/ecommerce/catalog/products.html",{'products':products})

def upload(request):
  
    #C
    if request.method == 'POST':
        name = request.POST.get('product_name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['image']
        quantity = request.POST.get('quantity')
        
        print(image)
        #Checking product upload form values are valid
        if name and price and description and image:
            # Create a new Product instance and assign values
            new_product = Product(name=name, price=price, description=description, image=image, quantity=quantity)
            new_product.save()  # Save the product to the database
            return redirect('products_list')  # Redirect to a confirmation page
            
    return HttpResponse(print(image))  


def new_products(request):
       return render(request,"backend/apps/ecommerce/catalog/add-product.html")


#reports view

def customer_orders(request):
    orders = Order.objects.all()
    context = {
        'orders':orders
    }
    return render(request,"backend/apps/ecommerce/reports/customer-orders.html",context)

def invoice_id_generator():
    # Define the characters and numbers you want to choose from
    characters = string.ascii_uppercase  # Uppercase letters
    numbers = string.digits  # Digits 0-9

    # Choose a random character and number
    random_character = random.choice(characters)
    random_number = ''.join(random.choice(numbers) for _ in range(5))  # Generates a 3-digit random number

    # Combine the character and number into the invoice number
    invoice_number = random_character + random_number
    return invoice_number

import datetime
def approval(request,id):

    order = Order.objects.filter(order_id=id).update(status='approved')
    user_id = request.session.get('user_id')
    order_id = Order.objects.get(order_id=id)
    email = Order.objects.get(order_id=id).email
    name = Customer.objects.get(Customer_Email=email).Customer_Name
   
    item = Cart.objects.filter(order_id=id)
  
    order_time = datetime.date.today()
    gateway = Order.objects.get(order_id=id).gateway
    
    #invoice
    invoice_id = invoice_id_generator()
    invoice = Invoice(invoice_id=invoice_id,order_date=datetime.date.today(),order_id=order_id,customer_name=name,email=email,gateway=gateway)
    #return HttpResponse(invoice_id)
    invoice.save()
    total = Order.objects.get(order_id=id).total
    subject = 'Invoice'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    bcc_list = [from_email]
    context = {
        'items':item,
        'email':email,
        'name':name,
        'gateway':gateway,
        #'order_date':order_date,
        'order_time':order_time,
        'total':total,
        'invoice_id':invoice_id
    }
    html_content = render_to_string('invoice.html',context)
    
    msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list,bcc_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

   
    return redirect('customer_orders')

def order_items(request):
    order_items = Cart.objects.all()

    return render(request,"backend/apps/ecommerce/reports/order-items.html",{'order_items':order_items})

def decline(request,id):
    Order.objects.filter(order_id=id).update(status='declined')
    email = Order.objects.get(order_id=id).email
    
    subject = 'Order Updates'
    from_email = settings.EMAIL_HOST_USER
    
    recipient_list = [email]
    context = {
        'order_id':id
    }
    html_content = render_to_string('order_decline.html',context)
    
    msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    return redirect('customer_orders')    

def returns(request):
    return render(request,"backend/apps/ecommerce/reports/returns.html")

def sales(request):


    approved = Order.objects.filter(status='approved').count()
    
    declined = Order.objects.filter(status='declined').count()
    
    pending = Order.objects.filter(status='pending').count()

    total_sales = Order.objects.filter(status='approved').aggregate(total_sum=models.Sum('total'))['total_sum']

    order_details =  Payment.objects.select_related('order_id').values(
        'order_id__order_id',
        'transaction_number',
        'order_id__order_date',
        'order_id__total',
        'order_id__gateway',
        'phone_number',

        )
    context={
        'order_details':order_details,
        'approved':approved,
        'declined':declined,
        'order':Order.objects.count(),

        'sales':total_sales
    }
    
    return render(request,"backend/dashboards/sales.html",context)



def shipping(request):
    return render(request,"backend/apps/ecommerce/reports/shipping.html")

def view(request):
    return render(request,"backend/apps/ecommerce/reports/view.html")

# account settings

def dashboard(request):

    customer_order = Order.objects.all()
    products = Product.objects.count()
    orders = Order.objects.count()
    customer = Customer.objects.count()
    total_sales = Order.objects.filter(status='approved').aggregate(total_sum=models.Sum('total'))['total_sum']

    approved = Order.objects.filter(status='approved').count()
    
    declined = Order.objects.filter(status='declined').count()
    
    pending = Order.objects.filter(status='pending').count()
  

    admin = Admin.objects.get(email = 'admin@example.com')
    context = {
        
        'products':products,
        'orders':orders,
        'customer':customer,
        'approved':approved,
        'declined':declined,
        'pending':pending,
        'admin':admin,
        'sales':total_sales,
        'customer_orders': customer_order

    }
  
    
    try:
        if request.method=='POST':
            request.session['admin_login'] = 'adminpassed'
            password = request.POST['password']
            
            condition1 = password==admin.password 
            condition2 = 'admin_login' in request.session and request.session['admin_login']
            if not condition1 :
                
                #return  render(request,"backend/index.html",context)
                messages.error(request,'Invalid Email/password. Please Try Again!')
                #return redirect('sign_in')
            elif not condition2:
                HttpResponse('please log in as admin')
            else:
                
                return  render(request,"backend/index.html",context)
                #return HttpResponse(admin.password)
                #return redirect('index')
    except admin.DoesNotExist: 
        messages.error(request,'invalid credential')
        #return  render(request,"backend/index.html",context)
        #return HttpResponse(request.POST.get('password'))
    return redirect('sign_in')
    return render(request,"backend/authentication/general(2)/sign-in.html")


#dashboard



