from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    Customer_Name = models.CharField(max_length=30)
    Customer_Email = models.CharField(max_length=50)
    Customer_Password = models.CharField(max_length=255)
    Customer_Confirm_Password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50,default='',null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    account_status = models.CharField(max_length=10, default='active')
    user_image = models.ImageField(upload_to="uploads",null=True,default=None)
    role = models.CharField(max_length=15,null=True)
    def is_active(self):
        return self.account_status == 'active'

    def is_inactive(self):
        return self.account_status == 'inactive'

class Customer_Info(models.Model):
    Phone_Number = models.CharField(max_length=20, primary_key=True )
    Facebook = models.CharField(max_length=30)
    Twitter = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Gender = models.CharField(max_length=6)


class Product(models.Model):
    name = models.CharField(max_length=255) 
    description = models.CharField(max_length=255,default="") 
    image = models.ImageField(upload_to="uploads",null=True,default=None)
    price = models.FloatField()
    quantity = models.IntegerField(null=True)
    status = models.CharField(max_length=255,null=True)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(null=True)
    customer_name = models.CharField(null=True,max_length=100)
    email = models.EmailField(null=True)
    status = models.CharField(null=True,max_length=100)
    total = models.FloatField(null=True)
    gateway = models.CharField(null=True,max_length=100)

    def is_pending(self):
        return self.status == 'pending'
    
    def is_approved(self):
        return self.status == 'approved'

class Invoice(models.Model):
    invoice_id = models.CharField(primary_key=True,max_length=10)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    order_date = models.DateField(null=True)
    customer_name = models.CharField(null=True,max_length=100)
    email = models.EmailField(null=True)
    gateway = models.CharField(null=True,max_length=100)
    

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    transaction_number = models.CharField(null=True,max_length=255)
    phone_number = models.CharField(null=True,max_length=255)
    email = models.EmailField(null=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    

from datetime import datetime

class Cart(models.Model):
   
   
    email = models.EmailField(null=True)
    item_name = models.CharField(null=True,max_length=100)
    item_price = models.CharField(null=True,max_length=100)
    total = models.FloatField(null=True)
    cart_session =models.FloatField(null=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)

  

class Admin(models.Model):
    name=models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)

# make migration pending for this model
class BlogPost(models.Model):
    author_name = models.CharField(max_length=100,null=True)  # You can adjust the max_length as needed.
    blog_title = models.CharField(max_length=200,null=True)   # You can adjust the max_length as needed.
    user_image = models.ImageField(upload_to="uploads/blogs",null=True,default=None)
    date = models.DateField(null=True)
    writing = models.TextField(null=True) 

class Blog_comment(models.Model):
    blog_id = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=100,null=True)
    comment = models.TextField(null=True)
    comment_date = models.DateField(null=True)

class Contact_message(models.Model):
    name =  models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(max_length=100,null=True)
    message_posted = models.DateField(null=True)
    
class Admin(models.Model):
    name=models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)