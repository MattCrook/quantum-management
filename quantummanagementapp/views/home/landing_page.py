from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required



def landing_page(request):
    if request.method == 'GET':
        template = 'landing_page.html'
        context = {}

        return render(request, template, context)


@login_required
def home(request):
    if request.method == 'GET':
        user = request.user
        # userdata = {
        #     'user_id': auth0user.uid,
        #     'name': user.first_name,
        #     'picture': auth0user.extra_data['picture'],
        #     'email': auth0user.extra_data['email'],
        # }
    # auth0user = user.social_auth.get(provider='auth0')
        template = 'home/home.html'
        context = {
            'user': user
            }

        return render(request, template, context)
