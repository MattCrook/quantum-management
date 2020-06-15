from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
