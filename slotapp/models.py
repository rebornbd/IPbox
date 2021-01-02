from django.db import models
from bladeapp.models import Blade


class Slot(models.Model):
  name    = models.CharField(max_length=128)
  ip      = models.GenericIPAddressField()
  blade   = models.ForeignKey(Blade, related_name="slots", on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = "Slots"
    
  def __str__(self):
    return self.name
