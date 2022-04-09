from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import  EmailMultiAlternatives

def send_login_mail(request,user):
    print('---------------->send_signup_otp_mail')
    current_site = get_current_site(request)
    subject = "Greetings From Test"
    signup = 'Test'
    to_email = [user.email]
    from_email = settings.EMAIL_HOST_USER
    # for production plese change http to https
    url =  "http://{}/user-login/{}".format(current_site,user.id)
    context =  ( {
        'username':user.fullname,
        'url':url
        } )
    html_content = render_to_string('accounts/send_user_login_mail.html', context)
    

    msg = EmailMultiAlternatives(subject=subject, body=signup, from_email=from_email, to=to_email)
    msg.attach_alternative( html_content , "text/html")
    email_sent_status = msg.send()

    return email_sent_status