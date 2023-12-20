from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages
from ..models import Customer
from django.contrib.sites.shortcuts import get_current_site
from django.utils.safestring import mark_safe
import secrets
import random
from django.http import HttpResponse
from django.shortcuts import render,redirect

verificationCode = None

#view for sending 2-FA mail
def mailtest(request):
    global verificationCode
    verificationCode = random.randint(1000, 9999)
    subject = 'Confirm your email address'
    from_email = settings.EMAIL_HOST_USER
    
    recipient_list = [request.session.get('email')]
    context = {'verificationCode': verificationCode}
    html_content = render_to_string('two-factor-mail.html',context)

    msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")

    #msg.send()
    if msg.send():
            success_message = mark_safe(
           f'Dear <b>user</b>, please check your email <b>{recipient_list}</b> Inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )
            messages.success(request, success_message)

               
    else:
            messages.error(request, f'There is a problem sending email to you, check if you typed it correctly.')
    return render(request, 'email_message.html')

def verify(request):
    code = request.POST.get('code')
    
    if code == str(verificationCode) and code is not None:
    
     
        return redirect('home.html')

    else:
     
        messages.error(request,'Invalid Code. Please Try Again!')
        return render(request,'2-FA.html')
    

def activate(request,token):
    
   
    name = request.session.get('name')
    email = request.session.get('email')
    password = request.session.get('password')
    c_password = request.session.get('c_password')

    Customer.objects.filter(Customer_Email=email).update(account_status='active')
    
        # Success message for complete registration
    messages.success(request, "Registration completed, now Log In to the system")
    return render(request,'login.html')

def activate_email(request):
   
        token = secrets.token_hex(10),
        subject = 'Confirm your email address'
        from_email = settings.EMAIL_HOST_USER
        email = request.session.get('email')
        name = request.session.get('name')
        password = request.session.get('password')
        c_password = request.session.get('c_password')
        recipient_list = [email]
        html_content = render_to_string('email.html', {
            #'User': User.name,
            'domain': get_current_site(request).domain,
            #'uid': urlsafe_base64_encode(force_bytes(name)),
            #'token': account_activation_token.make_token(name),
            'token': token,
            "protocol": 'https' if request.is_secure() else 'http'
        })
        msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        #msg.send()

        if msg.send():
            success_message = mark_safe(
           f'Dear <b>user</b>, please check your email <b>{email}</b> inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )
            messages.success(request, success_message)

               
        else:
            messages.error(request, f'There is a problem sending email to you, check if you typed it correctly.')

def forgotPassword(request):
        token = secrets.token_hex(10),
        subject = 'Password reset link'
        from_email = settings.EMAIL_HOST_USER
        email = request.session.get('email')
        name = request.session.get('name')
        password = request.session.get('password')
        c_password = request.session.get('c_password')
        recipient_list = [email]
        html_content = render_to_string('forget-pass-mail.html', {
            #'User': User.name,
            'domain': get_current_site(request).domain,
            #'uid': urlsafe_base64_encode(force_bytes(name)),
            #'token': account_activation_token.make_token(name),
            'token': token,
            "protocol": 'https' if request.is_secure() else 'http'
        })
        msg = EmailMultiAlternatives(subject, html_content, from_email, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        #msg.send()

        if msg.send():
            success_message = mark_safe(
           f'Dear <b>user</b>, please check your email <b>{email}</b> inbox and click on the received confirmation link to activate your account and complete the registration. <b>Note:</b> check your spam folder.'
    )
            messages.success(request, success_message)

               
        else:
            messages.error(request, f'Problem sending email to you, check if you typed it correctly.')    

def changePassword(request,token):
     email = email = request.session.get('email')
     return render(request,'change_password.html',{'usermail':email})