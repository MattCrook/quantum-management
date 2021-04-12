from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import SignUpForm
from quantummanagementapp.models import AdminUser, Image
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.messages import error, success, INFO
from rest_framework.authtoken.models import Token
from quantummanagementapp.models import CredentialsModel
from social_django.models import UserSocialAuth, DjangoStorage
import json



@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)

            social_user = UserSocialAuth.create_social_auth(user, user.id, 'quantummanagement')
            credential = {
                'username': user.username,
                'password': user.password,
            }
            credentials = CredentialsModel(user=user, credentials=credential)
            django_token = Token.objects.get(user=user)

            extra_data = {
                "token": django_token.key,
                # "credentials": credentials,
            }
            social_user.extra_data = extra_data
            social_user.save()
            credentials.save()

            login(request, user)
            return redirect(reverse('quantummanagementapp:home'))
        else:
            print("Register Errors", form.errors.as_data())
            error_messages = form.errors
            messages.add_message(request, messages.ERROR, error_messages)
            return redirect(reverse('quantummanagementapp:register'))

    else:
        admin_users = AdminUser.objects.all()
        form = SignUpForm()
        template = 'registration/register.html'
        context = {
            'admin_users': admin_users,
            'form': form
        }
        return render(request, template, context)
