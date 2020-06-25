from django.db import models
from quantummanagementapp.models import AdminUser

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin_user.user.first_name
