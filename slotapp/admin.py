from django.contrib import admin
from .models import Slot

myModels = [Slot]
admin.site.register(myModels)
