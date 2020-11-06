from django.db import models
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage
from django.db import models
from rest_framework.authtoken.models import Token



# fs = FileSystemStorage(location='../media/photos')
# picture = models.ImageField(storage=fs, blank=True, null=True)

class AdminUser(models.Model):

    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    image = models.ForeignKey("Image", blank=True, null=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("adminUser")
        verbose_name_plural = ("adminUsers")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.role}'

    def get_absolute_url(self):
        return reverse("admin_user_details", kwargs={"pk": self.pk})

@receiver(post_save, sender=User)
def create_admin_user(sender, instance, created, **kwargs):
    if created:
        AdminUser.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_admin_user(sender, instance, **kwargs):
    instance.user.save()
