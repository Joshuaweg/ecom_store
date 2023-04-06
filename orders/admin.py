from django.contrib import admin
from . import models

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id",)

admin.site.register(models.Order, OrderAdmin)