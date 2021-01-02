from django.db import models

class Cluster(models.Model):
  name        = models.CharField(max_length=128)
  ip          = models.GenericIPAddressField()
  lb_ip       = models.GenericIPAddressField()
  bootstrap   = models.GenericIPAddressField()

  class Meta:
    verbose_name_plural = "Clusters"
    
  def __str__(self):
    return self.name
