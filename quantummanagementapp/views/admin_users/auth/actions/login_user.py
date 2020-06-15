from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login, admin

def login_user(request):
    login(request)
    return redirect(reverse('quantummanagementapp:home'))

def admin_user(request):
    admin(request)
    return redirect(reverse('quantummanagementapp:admin'))
