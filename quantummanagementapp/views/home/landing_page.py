from django.shortcuts import render, redirect, reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quantummanagementapp.models import AdminUser
# from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from quantummanagementapp.models import CredentialsModel
from httplib2 import Http
from social_django.models import UserSocialAuth, DjangoStorage
import json



def landing_page(request):
    user = request.user
    if user.is_authenticated:
        return redirect(reverse('quantummanagementapp:home'))
    else:
        return render(request, 'landing_page.html')



@login_required
def home(request):
    if request.method == 'GET':
        user = request.user
        if user and hasattr(user, 'social_auth'):
            is_social_auth = user.social_auth.get(user_id=user.id)
            if is_social_auth is not None:
                social_user = is_social_auth
                provider = social_user.provider
                print('provider', provider)
                if provider == 'auth0':
                    auth0user = user.social_auth.get(provider='auth0')
                    userdata = {
                        'user_id': auth0user.uid,
                        'name': user.first_name,
                        'picture': auth0user.extra_data['picture'],
                        'email': auth0user.extra_data['email'],
                        'token': auth0user.extra_data['access_token']
                    }
                    print("USERDATA", userdata)
                    user_id = auth0user.user_id
                    quantum_user = User.objects.get(pk=user_id)
                    admin_user = AdminUser.objects.get(user_id=user_id)

                    return render(request, 'home/home.html', {
                        'auth0User': auth0user,
                        'userdata': json.dumps(userdata, indent=4),
                        'user': quantum_user,
                        'admin_user': admin_user,
                    })

                elif provider == 'google-oauth2':
                    user_data = User.objects.get(username=user)
                    user_id = user_data.id
                    admin_user = AdminUser.objects.get(user_id=user_id)
                    status = True

                    if not request.user.is_authenticated:
                        return HttpResponseRedirect('login')

                    storage = DjangoORMStorage(CredentialsModel, 'user_id', request.user, 'credential')
                    credential = storage.get()
                    try:
                        access_token = credential.access_token
                        resp, cont = Http().request("https://www.googleapis.com/auth/gmail.readonly",
                                                    headers={'Host': 'www.googleapis.com',
                                                            'Authorization': access_token})
                    except:
                        status = False
                        print('Not Found')

                    template = 'home/home.html'
                    context = {
                        'user': user_data,
                        'admin_user': admin_user,
                        'status': status,
                        'credential': credential
                    }
                    return render(request, template, context)

                elif provider == 'quantummanagement':
                    user = User.objects.get(pk=user.id)
                    admin_user = AdminUser.objects.get(user_id=user.id)
                    social_user = user.social_auth.get(provider='quantummanagement')
                    session = request.session.session_key
                    django_token = Token.objects.get(user=user)
                    # credentials = CredentialsModel.objects.get(user_id=user.id)
                    # storage = DjangoORMStorage(CredentialsModel, 'user_id', request.user, 'credential')
                    # print(storage)
                    # key = storage.key_name
                    # val = storage.key_value
                    # prop = storage.property_name

                    # print(key)
                    # print(val)
                    # print(prop)
                    # credentials = storage.get()
                    # print("CREDENTIALS", credentials)

                    extra_data = {
                        "session": session,
                        "token": django_token.key,
                        # "credentials": credentials,
                        # "credential": credentials.credential,
                    }

                    template = 'home/home.html'
                    context = {
                            'user': user,
                            'admin_user': admin_user,
                            'extra_data': extra_data,
                        }

                    return render(request, template, context)

                else:
                    user = User.objects.get(pk=user.id)
                    admin_user = AdminUser.objects.get(user_id=user.id)
                    social_user = user.social_auth.get(provider='facebook')
                    session = request.session.session_key
                    django_token = Token.objects.get(user=user)
                    credentials = CredentialsModel.objects.get(user_id=user.id)

                    extra_data = {
                        "session": session,
                        "token": django_token.key,
                        "credentials": credentials,
                        "credential": credentials.credential,
                    }

                    template = 'home/home.html'
                    context = {
                            'user': user,
                            'admin_user': admin_user,
                            'extra_data': extra_data,
                        }

                    return render(request, template, context)

            else:
                user_data = User.objects.get(username=user)
                user_id = user_data.id
                admin_user = AdminUser.objects.get(user_id=user_id)
                template = 'home/home.html'
                context = {
                    'user': user_data,
                    'admin_user': admin_user,
                    'status': status
                }
            return render(request, template, context)

        else:
            Response({'message': 'User has no attribute social_auth.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            template = 'landing_page.html'
            context = {}
            return render(request, template, context)
