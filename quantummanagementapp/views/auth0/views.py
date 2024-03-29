# import json
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout as log_out
# from django.conf import settings
# from django.http import HttpResponseRedirect
# from urllib.parse import urlencode
# from django.contrib.auth import logout as django_logout



@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

#     return render(request, 'dashboard.html', {
#         'auth0User': auth0user,
#         'userdata': json.dumps(userdata, indent=4)
#     })

# handler for the "index" view in your views.py to render the index.html if the user needs to log in.
# If the user is already logged in, the "dashboard" view will be shown instead.
# def index(request):
#     user = request.user
#     if user.is_authenticated:
#         return redirect(dashboard)
#     else:
#         return render(request, 'index.html')


# logout method to clear the session and redirect the user to the Auth0 logout endpoint.
# def logout(request):
#     log_out(request)
#     return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
#     logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
#                  (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
#     return HttpResponseRedirect(logout_url)


# uses the django_logout function provided by Django to log out from your application.
# Then, it redirects your user to the logout URL provided by Auth0 to log out from the identity provider
# def logout(request):
#     django_logout(request)
#     domain = '<YOUR-AUTH0-DOMAIN>'
#     client_id = '<YOUR-AUTH0-CLIENT-ID>'
#     return_to = 'http://localhost:8000'
#     return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')
