from datetime import datetime
from enum import unique
from django.db import models

# Create your models here.

class TradeRequest(models.Model):
    buyer = models.CharField(max_length=50)
    seller = models.CharField(max_length=50)
    unique_id = models.CharField(max_length=20)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    exchange_rate = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now)
