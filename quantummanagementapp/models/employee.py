from django.db import models
from django.urls import reverse
from django.db.models import F
from quantummanagementapp.models import AdminUser
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE



class Employee(SafeDeleteModel):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    compensation = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    is_salary = models.BooleanField(null=True, blank=True)
    is_hourly = models.BooleanField(null=True, blank=True)
    admin_user_id = models.ForeignKey(AdminUser, on_delete=models.CASCADE)

    _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = (F('start_date').desc(nulls_last=True),)
        verbose_name = ("employee")
        verbose_name_plural = ("employees")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("employee_details", kwargs={"pk": self.pk})
