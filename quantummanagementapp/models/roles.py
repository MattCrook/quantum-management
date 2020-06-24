from django.db import models


class Roles(models.Model):

    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = ("role")
        verbose_name_plural = ("roles")

    def __str__(self):
        return f'{self.name}'
