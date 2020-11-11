from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField


class CredentialsModel(models.Model):
    user = models.OneToOneField(User, primary_key=True, default='', on_delete=models.CASCADE)
    credential = CredentialsField()
    task = models.CharField(max_length=80, blank=True, null=True)
    updated_time = models.CharField(max_length=80, blank=True, null=True)


class CredentialsAdmin(admin.ModelAdmin):
    pass
