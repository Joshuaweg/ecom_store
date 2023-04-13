from django.contrib import admin
from . import models

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id",)


class CartAdmin(admin.ModelAdmin):
    list_display = ("id",)


class CartTableAdmin(admin.ModelAdmin):
    list_display = ("id",)


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartProductTable, CartTableAdmin)
