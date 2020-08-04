from django.db import models
from django.utils import timezone
from django.db.models import F
from quantummanagementapp.models import Attraction
from django.urls import reverse
from . import Park


class AttractionWaitTimes(models.Model):

    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    current_wait_time = models.DurationField()
    timestamp = models.DateTimeField(default=timezone.now)
    park = models.ForeignKey(Park, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("waittime")
        verbose_name_plural = ("waittimes")
        ordering = (F('current_wait_time').desc(nulls_last=True),)

    def __str__(self):
        return f'{self.attraction.name} {self.current_wait_time}'

    def get_absolute_url(self):
        return reverse("attraction_wait_times_details", kwargs={"pk": self.pk})
