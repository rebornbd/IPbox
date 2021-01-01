
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'rackapp'

urlpatterns = [
  path('create', views.rackCreate, name='rack_create'),
  path('update/<id>', views.rackUpdate, name='rack_update'),
  path('rackquery/<id>', views.rackQuery, name='rack_query'),
  path('', views.rackList, name="racks"),
]
