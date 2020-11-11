from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import login, admin
from django.views.decorators.csrf import csrf_exempt
from quantummanagementapp.models import LoginForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.messages import error, success, INFO
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
import json



def admin_user(request):
    admin(request)
    return redirect(reverse('quantummanagementapp:admin'))


def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # print(login_form)
        # if login_form.is_valid():
        #     login_form.save()
            # username = login_form.cleaned_data.get('username')
            # password = login_form.cleaned_data.get('password')
        username = request.POST['username']
        password = request.POST['password']
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            login(request, authenticated_user)
            return redirect(reverse('quantummanagementapp:home'))
        else:
            data = json.dumps({"valid": False})
            # return HttpResponse(data, content_type='application/json')
            print("LOGINDATA", login_form.errors.as_data())
            error_message = login_form.errors.as_data()
            messages.add_message(request, messages.ERROR, error_message)
            return redirect(reverse('quantummanagementapp:login'))

    else:
        login_form = LoginForm()
        template = 'registration/login.html'
        context = {
            'login_form': login_form
        }
        return render(request, template, context)
