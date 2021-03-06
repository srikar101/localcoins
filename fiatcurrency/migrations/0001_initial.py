# Generated by Django 4.0.1 on 2022-02-14 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FiatCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiat_name', models.CharField(max_length=30)),
                ('fiat_code', models.CharField(max_length=20)),
                ('fiat_symbol', models.CharField(max_length=10)),
                ('fiat_rate', models.IntegerField()),
                ('fiat_status', models.CharField(max_length=20)),
            ],
        ),
    ]
