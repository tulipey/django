# Generated by Django 4.0.3 on 2022-05-06 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TD1App', '0003_alter_baka_baptiste_nom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BAKA_BAPTISTE',
        ),
        migrations.AddField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac', 'Server - Simple Server to deploy virtual machines'), ('Switch', 'Switch - To maintains and connect servers')], default='PC', max_length=32),
        ),
        migrations.AddField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 6, 9, 47, 12, 241875)),
        ),
    ]