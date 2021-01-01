from django.contrib import admin
from .models import Blade

myModels = [Blade]
admin.site.register(myModels)
