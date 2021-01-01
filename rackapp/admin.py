from django.contrib import admin
from .models import Rack

myModels = [Rack]
admin.site.register(myModels)
