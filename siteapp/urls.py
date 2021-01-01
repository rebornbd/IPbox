
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'siteapp'

urlpatterns = [
  path('site/create', views.siteCreate, name='site_create'),
  path('site/update/<id>', views.siteUpdate, name='site_update'),
  path('sites', views.siteList, name="sites"),
]
