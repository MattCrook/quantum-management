from django.db import models
from django.urls import reverse


class AttractionType(models.Model):

    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = ("attractiontype")
        verbose_name_plural = ("attractiontypes")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("attraction_type_details", kwargs={"pk": self.pk})
