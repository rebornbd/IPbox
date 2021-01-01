from django.db import models
from siteapp.models import Site
from rackapp.models import Rack


class Blade(models.Model):
  name    = models.CharField(max_length=128)
  ip      = models.GenericIPAddressField()
  rack    = models.ForeignKey(Rack, related_name="blades", on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = "Blades"

  def __str__(self):
    return self.name
