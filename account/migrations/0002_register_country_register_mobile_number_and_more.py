# Generated by Django 4.0.2 on 2022-02-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='country',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='register',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
