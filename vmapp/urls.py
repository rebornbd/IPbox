
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'vmapp'

urlpatterns = [
  path('create', views.vmCreate, name='vm_create'),
  path('update/<id>', views.vmUpdate, name='vm_update'),
  path('vmquery/<id>', views.vmQuery, name='vm_query'),
  path('', views.vmList, name="vms"),
]
