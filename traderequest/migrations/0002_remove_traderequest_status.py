# Generated by Django 4.0.2 on 2022-02-24 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traderequest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traderequest',
            name='status',
        ),
    ]
