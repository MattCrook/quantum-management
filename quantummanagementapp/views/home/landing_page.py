from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quantummanagementapp.models import AdminUser
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.http import HttpResponseRedirect
from quantummanagementapp.models import CredentialsModel
from httplib2 import Http
from social_django.models import UserSocialAuth, DjangoStorage
import json




def landing_page(request):
    if request.method == 'GET':
        template = 'landing_page.html'
        context = {}

        return render(request, template, context)


@login_required
def home(request):
    if request.method == 'GET':
        user = request.user
        if user and hasattr(user, 'social_auth'):
            is_social_auth = user.social_auth.filter(user_id=user.id).first()
            if is_social_auth is not None:
                social_user = is_social_auth
                if social_user is not None:
                    provider = social_user.provider
                    if provider == 'auth0':
                        auth0user = user.social_auth.get(provider='auth0')
                        userdata = {
                            'user_id': auth0user.uid,
                            'name': user.first_name,
                            'picture': auth0user.extra_data['picture'],
                            'email': auth0user.extra_data['email'],
                        }
                        user_id = auth0user.user_id
                        quantum_user = User.objects.get(pk=user_id)
                        admin_user = AdminUser.objects.get(user_id=user_id)

                        return render(request, 'home/home.html', {
                            'auth0User': auth0user,
                            'userdata': json.dumps(userdata, indent=4),
                            'user': quantum_user,
                            'admin_user': admin_user,
                        })

                    elif provider == 'google':
                        user_data = User.objects.get(username=user)
                        user_id = user_data.id
                        admin_user = AdminUser.objects.get(user_id=user_id)
                        status = True

                        if not request.user.is_authenticated:
                            return HttpResponseRedirect('login')

                        storage = DjangoORMStorage(CredentialsModel, 'uid', request.user, 'credential')
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
                            'status': status
                        }
                        return render(request, template, context)

                    else:
                        user_data = User.objects.get(username=user)
                        user_id = user_data.id
                        admin_user = AdminUser.objects.get(user_id=user_id)
                        status = True

                        if not request.user.is_authenticated:
                            return HttpResponseRedirect('login')

                        # storage = DjangoORMStorage(CredentialsModel, 'user_id', request.user, 'credential')
                        # credential = storage.get()
                        # try:
                        #     access_token = credential.access_token
                        #     resp, cont = Http().request("https://www.googleapis.com/auth/gmail.readonly",
                        #                                 headers={'Host': 'www.googleapis.com',
                        #                                         'Authorization': access_token})
                        # except:
                        #     status = False
                        #     print('Not Found')

                        template = 'home/home.html'
                        context = {
                            'user': user_data,
                            'admin_user': admin_user,
                            'status': status
                        }

                        return render(request, template, context)
            else:
                user = User.objects.get(pk=user.id)
                admin_user = AdminUser.objects.get(user_id=user.id)
                social_user = UserSocialAuth.create_social_auth(user, user.id, 'quantummanagement')
                session = request.session.session_key
                # session_data = request.session.session_data

                django_token = Token.objects.get(user=user)
                creds = {
                    'username': user.username,
                    'password': user.password,
                }
                credentials = CredentialsModel(user=user, credential=creds)

                extra_data = {
                    "session": session,
                    "token": django_token.key,
                    "credentials": credentials.credential,
                }
                social_user.extra_data = extra_data
                social_user.save()
                credentials.save()
                template = 'home/home.html'
                context = {
                        'user': user,
                        'admin_user': admin_user,
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
