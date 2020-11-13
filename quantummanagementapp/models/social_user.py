from django.db import models
from social_django.models import AbstractUserSocialAuth, DjangoStorage, USER_MODEL
from django.contrib.auth.models import User



class CustomUserSocialAuth(AbstractUserSocialAuth):
    social_user = models.ForeignKey(USER_MODEL, related_name='custom_social_auth', on_delete=models.CASCADE)
    django_user = models.ForeignKey(User, on_delete=models.CASCADE)



class CustomDjangoStorage(DjangoStorage):
    user = CustomUserSocialAuth
