from django.db import models

# Create your models here.

class PaymentWindows(models.Model):
    time = models.CharField(max_length=30)