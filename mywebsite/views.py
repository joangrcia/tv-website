from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from .decorators import logout_required
from captcha.fields import ReCaptchaField


from django.contrib import messages
from .tokens import account_activation_token


# from .forms import UserCreationForm
from .forms import CustomUserCreationForm

def index(request):
    context = {
        'title':'TraderVibes',
        'judul':'Selamat Datang',
        'subheading':'di TraderVibes'
    }
    user = None

    # print(request.user.is_authenticated)

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect ('dashboard:index')
        else:
            return render(request, 'index.html', context)

    if request.method == 'POST':
        
        username_login = request.POST.get('username')
        password_login = request.POST.get('password')

        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            messages.info(request, "Username or password incorrect.")
            return redirect('login')

    # return render(request, 'index.html', context)

def tampilan_404(request, exception):
    return render(request, '404.html', status=404)

def emailcheck(request):
    context = {
        'form':'email',
    }

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect ('dashboard:index')
        else:
            # return render(request, 'index.html', context)
            return render(request, 'emailcheck.html', context)

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on \
                received activation link to confirm and complete the registration. Note: Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Validasi CAPTCHA
            if form.cleaned_data.get('captcha'):
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                activateEmail(request, user, form.cleaned_data.get('email'))
                return redirect('emailcheck')
            else:
                messages.error(request, "Captcha verification failed. Please try again.")
        else:
            messages.error(request, "Please correct the following errors:")
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

            return redirect('signup')
        
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
    
def not_found(request):
    context = {'title':'Not Found'}
    return render(request, 'notfound.html', context)

def index_chart(request):
    context = {'title':'Not Found'}
    return render(request, 'chart.html', context)

def index_logout(request):
    context = {'title':'Not Found'}
    return render(request, 'logout.html', context)
    