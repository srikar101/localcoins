from datetime import datetime
from locale import currency
from django.db import models

# Create your models here.

class Wallet(models.Model):
    currency = models.CharField(max_length=30)
    generated_datetime = models.DateTimeField(default=datetime.now)
    wallet_address = models.CharField(max_length=100)

    def __str__(self):
        return self.currency