from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom Users Table"""
    email_code = models.IntegerChoices(default=0, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)
