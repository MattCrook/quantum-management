from django.db import models
from django.urls import reverse


class EmployeeAttraction(models.Model):

    employee = models.ForeignKey("Employee", related_name="employee", on_delete=models.CASCADE)
    attraction = models.ForeignKey("Attraction", related_name="attraction", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("employeeattraction")
        verbose_name_plural = ("employeeattractions")

    def get_absolute_url(self):
        return reverse("employee_attraction_details", kwargs={"pk": self.pk})
