from datetime import datetime
from django.db import models

# Create your models here.

class FiatGateways(models.Model):
    gateways_name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    supported_currencies = models.IntegerField(default=0)
    created_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.gateways_name