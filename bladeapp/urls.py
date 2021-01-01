
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'bladeapp'

urlpatterns = [
  path('create', views.bladeCreate, name='blade_create'),
  path('update/<id>', views.bladeUpdate, name='blade_update'),
  path('', views.bladeList, name="blades"),
]
