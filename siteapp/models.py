from django.db import models


class Site(models.Model):
  name = models.CharField(max_length=128)

  class Meta:
    verbose_name_plural = "Sites"

  def __str__(self):
    return self.name
