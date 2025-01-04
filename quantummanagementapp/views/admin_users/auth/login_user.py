from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import login, admin
# from django.views.decorators.csrf import csrf_exempt
from quantummanagementapp.models import LoginForm
from django.contrib.auth import authenticate
from django.contrib import messages
# from django.contrib.messages import error, success, INFO
from rest_framework.authtoken.models import Token
# from django.http import HttpResponse, HttpResponseBadRequest
# from social_core.backends.oauth import BaseOAuth1, BaseOAuth2
# from social_django.utils import psa
import json
#import os
from quantummanagement import settings




def admin_user(request):
    admin(request)
    return redirect(reverse('quantummanagementapp:admin'))


def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})

            if settings.ENVIRONMENT == 'development':
                print("LOGIN FORM: Login token data: ", data)

            login(request, authenticated_user)
            return redirect(reverse('quantummanagementapp:home'))
        else:
            # data = json.dumps({"valid": False})
            # return HttpResponse(data, content_type='application/json')
            if settings.ENVIRONMENT == 'development':
                print("LOGIN ERROR DATA: Login Form: ", login_form.errors.as_data())

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


# @psa('social:complete')
# def ajax_auth(request, backend):
#     """AJAX authentication endpoint"""
#     if isinstance(request.backend, BaseOAuth1):
#         token = {
#             'oauth_token': request.REQUEST.get('access_token'),
#             'oauth_token_secret': request.REQUEST.get('access_token_secret'),
#         }
#     elif isinstance(request.backend, BaseOAuth2):
#         token = request.REQUEST.get('access_token')
#     else:
#         raise HttpResponseBadRequest('Wrong backend type')
#     user = request.backend.do_auth(token, ajax=True)
#     login(request, user)
#     data = {'id': user.id, 'username': user.username}
#     return HttpResponse(json.dumps(data), mimetype='application/json')
