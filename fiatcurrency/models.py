from django.db import models

# Create your models here.

class FiatCurrency(models.Model):
    fiat_name = models.CharField(max_length=30)
    fiat_code = models.CharField(max_length=20)
    fiat_symbol = models.CharField(max_length=10)
    fiat_rate = models.FloatField()

    def __str__(self):
        return f'FiatCurrency : {self.fiat_name}'