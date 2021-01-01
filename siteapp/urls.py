
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'siteapp'

urlpatterns = [
  path('create', views.siteCreate, name='site_create'),
  path('update/<id>', views.siteUpdate, name='site_update'),
  path('sitequery/<id>', views.siteQuery, name='site_query'),
  path('', views.siteList, name="sites"),
]
