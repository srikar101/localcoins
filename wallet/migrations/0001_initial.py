# Generated by Django 4.0.1 on 2022-02-15 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=30)),
                ('generated_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('wallet_address', models.CharField(max_length=100)),
            ],
        ),
    ]