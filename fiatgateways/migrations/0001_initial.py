# Generated by Django 4.0.1 on 2022-02-15 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fiatgateways',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gateways_name', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30)),
                ('supported_currencies', models.IntegerField(default=0)),
                ('status', models.BooleanField()),
                ('created_datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
