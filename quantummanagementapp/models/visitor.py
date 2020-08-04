from django.db import models
from django.utils import timezone
from django.db.models import F
from django.urls import reverse
from . import Park



class Visitor(models.Model):

    check_in = models.DateTimeField(auto_now=False, default=timezone.now)
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    park = models.ForeignKey(Park, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = (F('check_in').asc(nulls_last=True),)
        verbose_name = ("visitor")
        verbose_name_plural = ("visitors")

    def __str__(self):
        return f'{self.check_in} - {self.ticket_price}'

    def get_absolute_url(self):
        return reverse("visitor_details", kwargs={"pk": self.pk})
