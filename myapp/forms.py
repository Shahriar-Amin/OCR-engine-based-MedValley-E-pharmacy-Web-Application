from django import forms

class Registration(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    email = forms.CharField(label='email', max_length=50)
    password = forms.CharField(label='tp_password', max_length=255)
    c_password = forms.CharField(label='tp_con_password', max_length=255)