from django.contrib import admin

# Register your models here.

from .models import Product, Country

admin.site.register(Product)
admin.site.register(Country)
