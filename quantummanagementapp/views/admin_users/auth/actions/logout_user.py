from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect(reverse('quantummanagementapp:landing_page'))
