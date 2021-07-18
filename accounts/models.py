from django.db import models


class UserProfile(models.Model):
    photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "User profiles"

