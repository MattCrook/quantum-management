import httplib2

from googleapiclient.discovery import build
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from quantummanagementapp.models import CredentialsModel
from quantummanagement import settings
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.shortcuts import render
from httplib2 import Http


# def home(request):
#     status = True

#     if not request.user.is_authenticated:
#         return HttpResponseRedirect('login')

#     storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
#     credential = storage.get()
#     try:
#         access_token = credential.access_token
#         resp, cont = Http().request("https://www.googleapis.com/auth/gmail.readonly",
#                                     headers={'Host': 'www.googleapis.com',
#                                             'Authorization': access_token})
#     except:
#         status = False
#         print('Not Found')

#     return render(request, 'home/home.html', {'status': status})


################################
#   GMAIL API IMPLEMENTATION   #
################################

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>


FLOW = flow_from_clientsecrets(
    settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
    scope='https://www.googleapis.com/auth/gmail.readonly',
    redirect_uri='http://127.0.0.1:8000/oauth2callback',
    prompt='consent')


def gmail_authenticate(request):

    if not request.user.is_authenticated:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SOCIAL_AUTH_GOOGLE_SECRET, request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)

    else:
        storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
        credential = storage.get()
        if credential is None or credential.invalid:
            FLOW.params['state'] = xsrfutil.generate_token(settings.SOCIAL_AUTH_GOOGLE_SECRET,
                                                            request.user)
            authorize_url = FLOW.step1_get_authorize_url()
            return HttpResponseRedirect(authorize_url)
        else:
            http = httplib2.Http()
            http = credential.authorize(http)
            service = build('gmail', 'v1', http=http)
            print('access_token = ', credential.access_token)
            status = True
            template = 'home/home.html'

            return render(request, template, {'status': status})


def auth_return(request):
    get_state = bytes(request.GET.get('state'), 'utf8')
    if not xsrfutil.validate_token(settings.SOCIAL_AUTH_GOOGLE_SECRET, get_state,
                                   request.user):
        return HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.GET.get('code'))
    storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
    storage.put(credential)
    print("access_token: %s" % credential.access_token)
    return HttpResponseRedirect("login/home")
