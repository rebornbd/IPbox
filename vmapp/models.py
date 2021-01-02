from django.db import models
from slotapp.models import Slot
from clusterapp.models import Cluster


class VM(models.Model):
  name      = models.CharField(max_length=128)
  hostname  = models.CharField(max_length=128)
  ip        = models.GenericIPAddressField()
  slot      = models.ForeignKey(Slot, related_name="vmslots", on_delete=models.CASCADE)
  cluster   = models.ForeignKey(Cluster, related_name='vmclusters', on_delete=models.CASCADE, blank=True, null=True)

  class Meta:
    verbose_name_plural = "VMs"
    
  def __str__(self):
    return self.name
