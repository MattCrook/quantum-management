from django.db import models
from django.forms.widgets import ClearableFileInput
from django import forms
from quantummanagementapp.models import AdminUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class Image(models.Model):
    image = models.ImageField(ClearableFileInput, upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.image


# @receiver(post_save, sender=AdminUser)
# def create_image(sender, instance, created, **kwargs):
#     if created:
#         Image.objects.create(image=instance)

# @receiver(post_save, sender=AdminUser)
# def save_image(sender, instance, **kwargs):
#     instance.image.save()
