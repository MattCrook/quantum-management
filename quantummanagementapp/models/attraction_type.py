from django.db import models


class AttractionType(models.Model):

    name = models.CharField(max_length=50)
    manufacturer = models.CharField()

    class Meta:
        verbose_name = ("attractiontype")
        verbose_name_plural = ("attractiontypes")

    def __str__(self):
        return f'{self.name}'
