from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    photo = models.CharField(max_length=200, blank=True, null=True)
    user  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile', blank=True, null=True)

    class Meta:
        verbose_name_plural = "User profiles"

