from django.contrib import admin
from .models import Device, Sede

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('id','name','country','company','business','type_sede')
    list_filter = ('name','country','company','business','type_sede')



   