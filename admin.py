from django.contrib import admin
from .models import CustomUser, Event


admin.site.register(CustomUser)
admin.site.register(Event)
