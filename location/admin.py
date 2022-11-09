from django.contrib import admin
from .models import Sede, Type_sede, Country, Company, Business, Zone

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)

@admin.register(Type_sede)
class Type_sedeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)



