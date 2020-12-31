from django.contrib import admin
from .models import Site

myModels = [Site]
admin.site.register(myModels)
