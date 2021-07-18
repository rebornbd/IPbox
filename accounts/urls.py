
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'accountsapp'

urlpatterns = [
  path('login', views.mylogin, name='login'),
  path('logout', views.mylogout, name='logout'),
  path('signup', views.mysignup, name='signup'),

  path('profile', views.userProfile, name='profile'),
]
