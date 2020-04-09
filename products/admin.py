from django.contrib import admin
from products.models import Products

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    class Meta:
        model = Products

admin.site.register(Products,ProductAdmin)

