from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from quantummanagementapp.models import AdminUser
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.http import HttpResponseRedirect
from quantummanagementapp.models import CredentialsModel
from httplib2 import Http





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
            social_user = user.social_auth.get(user_id=user.id)
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
            else:
                user_data = User.objects.get(username=user)
                user_id = user_data.id
                admin_user = AdminUser.objects.get(user_id=user_id)
                status = True

                if not request.user.is_authenticated:
                    return HttpResponseRedirect('login')

                storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
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
            template = 'home/home.html'
            context = {
                'user': user_data,
                'admin_user': admin_user,
                'status': status
            }

            return render(request, template, context)
