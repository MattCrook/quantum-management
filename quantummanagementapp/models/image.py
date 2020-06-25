from django.db import models
from quantummanagementapp.models import AdminUser

class Image(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image
