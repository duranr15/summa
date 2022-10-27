from django.contrib import admin
from .models import Device, Sede

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    pass