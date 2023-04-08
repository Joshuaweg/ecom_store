from django.db import models
from django.contrib.auth import get_user_model


class CreditCard(models.Model):
    credit_card_number = models.IntegerField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cvv = models.IntegerField(max_length=3)


class UserCreditCard(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
