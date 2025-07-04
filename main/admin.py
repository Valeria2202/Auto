# -- coding: utf-8 --
from django.contrib import admin
from .models import Client, Car, Sale

admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'price')

admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('client', 'car', 'created_at')

admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Sale)

