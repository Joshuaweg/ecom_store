from django.contrib import admin
from . import models

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductImage, ProductImageAdmin)
