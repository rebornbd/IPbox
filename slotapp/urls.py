
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'slotapp'

urlpatterns = [
  path('create', views.slotCreate, name='slot_create'),
  path('update/<id>', views.slotUpdate, name='slot_update'),
  path('slotquery/<id>', views.slotQuery, name='slot_query'),
  path('', views.slotList, name="slots"),
]
