from django.db import models
from django.forms.widgets import ClearableFileInput
from django import forms


class Image(models.Model):
    image = models.ImageField(ClearableFileInput, upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.image
