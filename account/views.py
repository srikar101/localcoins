from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings


from account.models import Register

# Create your views here.

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    email_body = render_to_string('mail_body.html',{
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject,body=email_body,
    from_email=settings.EMAIL_FROM_USER,to=[user.email])

    email.send()

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        country = request.POST['country']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        val1 = Register.objects.filter(username=username).exists()
        val2 = Register.objects.filter(email=email).exists()
        error_message = None
        message = None
        if val1:
            error_message = 'username already exist'
            return redirect('register')
        elif val2:
            error_message = 'email already exists'
            return redirect('register')
        else:
            user = Register(username=username,email=email,password=password1,mobile_number=mobile_number,country=country)
            user.password = make_password(user.password)
            user.save()

            send_activation_email(user, request)
            message = 'We have sent a link to your mail'

            return render(request,'register.html',{'error_message': error_message, 'message': message})
    else:
        return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        error_message = None
        try:
            match = Register.objects.filter(email=email).exists()
            user = Register.objects.get(email=email)
        except:
            error_message = 'Invalid credentials'
    
        
        if match:
            flag = check_password(password , user.password)
            if not user.is_email_verified:
                error_message = 'Your email is not verified, please check the email inbox and verify.'
                return render(request,'login.html', {'message': error_message})

            if flag:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                request.session['username'] = user.username
                return redirect('user_auth')
            else:
                error_message = 'Incorrect password'
                return render(request,'login.html', {'error_message': error_message})
        else:
            print('Invalid credentials')
            return render(request,'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')



def logout_view(request):
    request.session.clear()
    print(request.session.get('username'))
    return render(request, 'home.html')


def activate_user(request, uid, token):
    message = None
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = Register.objects.get(pk=uid)
    except:
        user=None

    if user and generate_token.check_token(user,token):
        user.is_email_verified=True
        user.save()

        message = "Email verification is successfully completed"

        return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'activate-failed.html')

    
    

