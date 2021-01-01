from django.db import models
from siteapp.models import Site


class Rack(models.Model):
  name  = models.CharField(max_length=128)
  ip    = models.GenericIPAddressField()
  site  = models.ForeignKey(Site, related_name="racks", on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = "Racks"

  def __str__(self):
    return self.name
