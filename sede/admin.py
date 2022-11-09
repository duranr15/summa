from django.contrib import admin
from .models import Country, Company, Sede, Type, Busines

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Busines)
class BusinesAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('name',)


