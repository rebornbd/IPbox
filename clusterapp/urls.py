
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'clusterapp'

urlpatterns = [
  path('create', views.clusterCreate, name='cluster_create'),
  path('update/<id>', views.clusterUpdate, name='cluster_update'),
  path('clusterquery/<id>', views.clusterQuery, name='cluster_query'),
  path('', views.clusterList, name="clusters"),
]
