from django.contrib import admin
from credit_cards import models

# Register your models here.


class CreditCardAdmin(admin.ModelAdmin):
    list_display = ("credit_card_number",)


class UserCreditCardAdmin(admin.ModelAdmin):
    list_display = ("user_id",)


admin.site.register(models.CreditCard, CreditCardAdmin)
admin.site.register(models.UserCreditCard, UserCreditCardAdmin)
