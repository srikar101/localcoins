from urllib import request
from django.db import models
from account.models import Register
from django.contrib.auth.models import User

# Create your models here.

class Advertisements(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=20)
    crypto_currency = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)
    currency = models.CharField(max_length=20,default='')
    margin = models.IntegerField(default=0)
    payment_window = models.CharField(max_length=20)
    min_limit = models.IntegerField(default=0)
    max_limit = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    payment_details = models.TextField()
    terms_of_trade = models.TextField()

    def __str__(self):
        return str(self.user)

