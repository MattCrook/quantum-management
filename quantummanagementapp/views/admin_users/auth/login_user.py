from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import login, admin
from django.contrib.auth.decorators import login_required


def login_user(request):
    login(request)
    return redirect(reverse('quantummanagementapp:home'))

def admin_user(request):
    admin(request)
    return redirect(reverse('quantummanagementapp:admin'))
