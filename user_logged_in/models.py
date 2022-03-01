from datetime import datetime
from xml.parsers.expat import model
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile_number = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.BigIntegerField()
    country = models.CharField(max_length=20)
    status = models.BooleanField()
    email_verification = models.BooleanField()
    sms_verification = models.BooleanField()
    status_2FA = models.BooleanField()
    verification_2FA = models.BooleanField()
    total_deposit_count = models.IntegerField(default=0)
    total_withdraw_count = models.IntegerField(default=0)
    total_transaction = models.IntegerField(default=0)
    created_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

