from django.db import models
from quantummanagementapp.models import Park, Attraction

class ParkAttractions(models.Model):

    park = models.ForeignKey(Park, related_name='parkinfo', on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, related_name='attractions', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("parkAttraction")
        verbose_name_plural = ("parkAttractions")
