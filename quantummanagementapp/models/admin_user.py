from django.db import models
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.models import User


class AdminUser(models.Model):

    user = models.OneToOneField(User, related_name="adminUser", on_delete=models.CASCADE)
    picture = models.ImageField(blank=True, null=True)
    role = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("adminUser")
        verbose_name_plural = ("adminUsers")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.role}'
