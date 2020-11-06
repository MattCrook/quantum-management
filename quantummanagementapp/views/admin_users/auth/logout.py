from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views

def logout_user(request):
    logout(request)
    # auth_views.auth_logout()
    auth_views.LogoutView()
    return redirect(reverse('quantummanagementapp:landing_page'))
