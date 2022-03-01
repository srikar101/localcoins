from django.db import models

# Create your models here.

class EmailTemplates(models.Model):
    etName = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)


class FAQ(models.Model):
    heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    
