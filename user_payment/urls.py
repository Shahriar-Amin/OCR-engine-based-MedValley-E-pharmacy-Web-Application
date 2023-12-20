from django.urls import path
from .import payment_views

urlpatterns = [
	path('product_page', payment_views.product_page, name='product_page'),
	path('payment_successful', payment_views.payment_successful, name='payment_successful'),
	path('payment_cancelled', payment_views.payment_cancelled, name='payment_cancelled'),
	path('stripe_webhook', payment_views.stripe_webhook, name='stripe_webhook'),
]