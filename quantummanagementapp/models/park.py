from django.db import models
from django.urls import reverse


class Park(models.Model):

    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    max_capacity = models.CharField(max_length=20, null=True, blank=True)
    number_of_attractions = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = ("park")
        verbose_name_plural = ("parks")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("park_details", kwargs={"pk": self.pk})
