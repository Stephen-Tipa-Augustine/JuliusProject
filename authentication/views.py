from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User, Permission, Group
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.contenttypes.models import ContentType
from . import forms
from . import models
import sendgrid
from sendgrid.helpers.mail import *


from .tokens import account_activation_token

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'auth_form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return render(request, 'auth/logout.html')

def activation_sent_view(request):
    return render(request, 'auth/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        username = user.username
        password = user.password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('homepage')
    else:
        return render(request, 'auth/activation_token_failed.html')

def register(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # Adding user a special permision
            content_type = ContentType.objects.get_for_model(models.Profile)
            special_perm = Permission.objects.get(
            codename='list_addition_ability',
            content_type=content_type,
            )
            user.user_permissions.add(special_perm)
            user.is_active = False
            user.save()
            # Sending user a confirmation link
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string('auth/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            sg = sendgrid.SendGridAPIClient(api_key='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')
            from_email = Email("tipancoders@gmail.com")
            to_email = To(user.profile.email)
            subject = subject
            content = Content("text/plain", message)
            mail = Mail(from_email, to_email, subject, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            if response.status_code == 202:
                emailSend = True
            else:
                emailSend = False
            return render(request, 'auth/activation_sent.html', {'username':user.username, 'emailSend':emailSend, 'mailResponse':response})
    else:
        form = forms.SignUpForm()
    return render(request, 'auth/register.html', {'userCreationForm': form})
def resendActivationLink(request, slug):
    user = get_object_or_404(User, username=str(slug))
    # Sending user a confirmation link
    current_site = get_current_site(request)
    subject = 'Please Activate Your Account'
    # load a template like get_template()
    # and calls its render() method immediately.
    message = render_to_string('auth/activation_request.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        # method will generate a hash value with user related data
        'token': account_activation_token.make_token(user),
    })
    sg = sendgrid.SendGridAPIClient(api_key='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')
    from_email = Email("tipancoders@gmail.com")
    to_email = To(user.profile.email)
    subject = subject
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    if response.status_code == 202:
        emailSend = True
    else:
        emailSend = False

    return render(request, 'auth/activation_sent.html', {'username': user.username, 'emailSend': emailSend})