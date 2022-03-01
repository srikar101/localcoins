from datetime import datetime
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Cryptocurrency(models.Model):
    crypto_name = models.CharField(max_length=50)
    crypto_image = models.ImageField(upload_to='crypto_pics')
    crypto_code = models.CharField(max_length=20)
    crypto_symbol = models.CharField(max_length=20)
    crypto_rate = models.FloatField()
    createddatetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'cryptocurrency : {self.crypto_name}'
