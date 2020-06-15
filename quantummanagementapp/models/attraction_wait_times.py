from django.db import models
from django.utils import timezone
from django.db.models import F
from quantummanagementapp.models import Attraction


class AttractionWaitTimes(models.Model):

    attraction = models.ManyToManyField(Attraction, on_delete=models.CASCADE)
    current_wait_time = models.DurationField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = ("waittime")
        verbose_name_plural = ("waittimes")
        ordering = (F('current_wait_time').desc(nulls_last=True),)

    def __str__(self):
        return f'{self.attraction.name} {self.current_wait_time}'
