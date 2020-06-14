from django.db import models
from django.utils import timezone
from django.db.models import F
from quantummanagementapp.models import Attraction

class AttractionVisitors(models.Model):

    visit_timestamp = models.DateTimeField(default=timezone.now)
    attraction  = models.ForeignKey(Attraction, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = (F('visit_timestamp').desc(nulls_last=True),)

    def __str__(self):
        return f'{self.attraction} - {self.visit_timestamp}'
