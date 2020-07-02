from django.db import models
from django.urls import reverse
from django.db.models import F
from quantummanagementapp.models import AdminUser
from datetimepicker.widgets import DateTimePicker
# from safedelete.models import SafeDeleteModel
# from safedelete.models import SOFT_DELETE
# from djmoney.models.fields import MoneyField




class Employee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    compensation =  models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8)
    pay_rate = models.CharField(null=True, blank=True, max_length=20)
    park = models.ForeignKey("Park", null=True, blank=True, on_delete=models.CASCADE)
    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE)

    # _safedelete_policy = SOFT_DELETE

    class Meta:
        ordering = (F('start_date').desc(nulls_last=True),)
        verbose_name = ("employee")
        verbose_name_plural = ("employees")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("employee_details", kwargs={"pk": self.pk})
