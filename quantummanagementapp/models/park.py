from django.db import models
# from django.urls import reverse
# from django.db.models import F
# from django.contrib.auth.models import AdminUser

class Park(models.Model):

    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    max_capacity = models.CharField()
    number_of_attractions = models.CharField()

    class Meta:
        verbose_name = ("park")
        verbose_name_plural = ("parks")

    def __str__(self):
        return f'{self.name}'
