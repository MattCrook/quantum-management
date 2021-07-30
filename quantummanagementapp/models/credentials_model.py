from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
# from oauth2client.contrib.django_util.models import CredentialsField
# from oauthlib.oauth2 import OAuth2Token, BearerToken
import datetime


class CredentialsModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # credentials = CredentialsField()
    task = models.CharField(max_length=80, blank=True, null=True)
    updated_time = models.TimeField(auto_now_add=True, null=True, blank=True)


# class CredentialsAdmin(admin.ModelAdmin):
#     pass
