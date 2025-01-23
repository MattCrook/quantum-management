import httplib2
#from googleapiclient.discovery import build
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from quantummanagementapp.models import CredentialsModel
from quantummanagement import settings
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.shortcuts import render
# from httplib2 import Http
import os


# Create a state token to prevent request forgery.
# Store it in the session for later validation.
# state = hashlib.sha256(os.urandom(1024)).hexdigest()
# session['state'] = state
# Set the client ID, token state, and application name in the HTML while
# serving it.
# response = make_response(
#     render_template('index.html',
#                     CLIENT_ID=CLIENT_ID,
#                     STATE=state,
#                     APPLICATION_NAME=APPLICATION_NAME))


# Ensure that the request is not a forgery and that the user sending
# this connect request is the expected user.
# if request.args.get('state', '') != session['state']:
#   response = make_response(json.dumps('Invalid state parameter.'), 401)
#   response.headers['Content-Type'] = 'application/json'
#   return response






FLOW = flow_from_clientsecrets(
    settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
    scope='https://www.googleapis.com/auth/gmail.readonly',
    # redirect_uri='http://127.0.0.1:8000/oauth2callback',
    redirect_uri='http://127.0.0.1:8000/complete/google-oath2/',
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
            #service = build('gmail', 'v1', http=http)
            if os.environ.get("")
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
