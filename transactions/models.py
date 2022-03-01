from datetime import datetime
from django.db import models
from account.models import Register

# Create your models here.

class Transactions(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    trx = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(default=datetime.now)
    amount = models.FloatField()
    post_balance = models.FloatField()
    detail = models.TextField(max_length=100)

    def __str__(self):
        return self.username