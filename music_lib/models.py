from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass 

class Album(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    artist = models.CharField(max_length=100, blank=True, null=True)
    creation_time = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.title



