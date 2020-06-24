from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from quantummanagementapp.models import SignUpForm
from django.http import HttpResponse

import json

from django.http import HttpResponse
from django.http import HttpResponseServerError
from quantummanagementapp.models import AdminUser, Employee

from django.contrib.auth.models import User
from rest_framework import status
from .login_user import login_user

def register_user(request):
    if request.method == 'GET':

        admin_users = AdminUser.objects.all()
        form = SignUpForm()

        template = 'registration/register.html'
        context = {
            'admin_users': admin_users,
            'form': form
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        new_user = User.objects.create_user(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            username=form_data['username'],
            email=form_data['email'],
        )
        new_user.save()

        new_admin_user = AdminUser.objects.create(
            # new_admin_user.pictue = form_data['picture'],
            # new_admin_user.role = form_data['role'],
            user_id=new_user.id
        )
        print("NAUSER", new_admin_user)

        new_admin_user.save()
        # username = form_data["username"]
        # raw_password = form_data["password1"]
        # user = authenticate(username=username, password=raw_password)
        return redirect(reverse('quantummanagementapp:login'))


# def register_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect(reverse('quantummanagementapp:home'))
#     else:
#         form = SignUpForm()
#         return render(request, 'registration/register.html', {'form': form})
