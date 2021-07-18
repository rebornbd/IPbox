from django.contrib import admin
from .models import UserProfile

myModels = [UserProfile]
admin.site.register(myModels)
