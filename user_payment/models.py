from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from myapp.models import Customer
# Create your models here.

class UserPayment(models.Model):
    Customer_ID = models.ForeignKey(Customer, default="", on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)

@receiver(post_save,sender=Customer)
def create_user_payment(sender,instance,created,**kwargs):
    if created:
        print() #UserPayment.objects.create(Customer=instance)
