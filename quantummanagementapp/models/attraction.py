from django.db import models
# from quantummanagementapp.models import AttractionType


class Attraction(models.Model):

    name = models.CharField(max_length=100)
    type = models.ForeignKey("AttractionType", null=True, blank=True, on_delete=models.CASCADE)
    capacity = models.CharField(max_length=20, null=True, blank=True)
    current_operating_capacity = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = ("attraction")
        verbose_name_plural = ("attractions")

    def __str__(self):
        return f'{self.name}'
