from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
# from oauth2client.contrib.django_util.models import CredentialsField
# from oauthlib.oauth2 import OAuth2Token, BearerToken
import datetime

# class CredentialsField(models.Field):
#     """Django ORM field for storing OAuth2 Credentials."""

#     def __init__(self, *args, **kwargs):
#         if 'null' not in kwargs:
#             kwargs['null'] = True
#         super(CredentialsField, self).__init__(*args, **kwargs)

class CredentialsModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credentials = models.CharField(max_length=10000, blank=True, null=True)
    task = models.CharField(max_length=80, blank=True, null=True)
    updated_time = models.TimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = ("credentials")
        verbose_name_plural = ("credentials")

    def __str__(self):
        return f'{self.user.email} {self.credentials} - {self.updated_time}'


class CredentialsAdmin(admin.ModelAdmin):
    pass
