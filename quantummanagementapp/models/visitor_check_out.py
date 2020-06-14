from django.db import models
from django.utils import timezone
from django.db.models import F

# auto_now_add sets the value of the field to current datetime when the object is created.
# auto_now sets the value of the field to current datetime every time the field is saved.
# These options and the default parameter are mutually exclusive.


class VisitorCheckOut(models.Model):

    checkout_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (F('checkout_timestamp').desc(nulls_last=True),)

    def __str__(self):
        return f'{self.checkout_timestamp}'
