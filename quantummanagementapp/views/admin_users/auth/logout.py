from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from quantummanagement import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode


def logout_user(request):
    user = request.user
    if user and hasattr(user, 'social_auth'):
        is_social_auth = user.social_auth.filter(user_id=user.id).first()
        if is_social_auth is not None:
            social_user = user.social_auth.filter(user_id=user.id).first()
            if social_user is not None:
                social_user = user.social_auth.get(user_id=user.id)
                provider = social_user.provider
                if provider == 'auth0':
                    auth0_logout(request)

                elif provider == 'facebook':
                    auth_views.auth_logout(request)

                elif provider == 'google':
                    auth_views.auth_logout(request)
                else:
                    logout(request)
        else:
            logout(request)
    else:
        logout(request)

    return redirect(reverse('quantummanagementapp:landing_page'))


# uses the django_logout function provided by Django to log out from your application.
# Then, it redirects your user to the logout URL provided by Auth0 to log out from the identity provider
# def auth0_logout(request):
#     django_logout(request)
#     domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
#     client_id = settings.SOCIAL_AUTH_AUTH0_KEY
#     return_to = 'http://localhost:8000'
#     return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')


# logout method to clear the session and redirect the user to the Auth0 logout endpoint.
def auth0_logout(request):
    logout(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)
