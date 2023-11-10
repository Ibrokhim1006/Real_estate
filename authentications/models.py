from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom Users Table"""
    email_code = models.IntegerField(null=True, blank=True)
    summ = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)


class PyemntSumm(models.Model):
    summ = models.CharField(max_length=20, null=True, blank=True)
    days = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.summ
