# Register your models here.
from django.contrib import admin
from .models import Bills_Products, Bills, Products, Clients, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Bills_Products)
admin.site.register(Bills)
admin.site.register(Products)
admin.site.register(Clients)

admin.site.register(CustomUser, UserAdmin)
