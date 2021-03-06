# Generated by Django 4.0.3 on 2022-05-24 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TD1App', '0006_auto_20220508_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='mach',
            field=models.CharField(choices=[('Technicien', 'Aime sa famille'), ('Directeur', 'Aime sa famille et l argent'), ('PDG', 'Aime l argent')], default='Technicien', max_length=32),
        ),
        migrations.AlterField(
            model_name='employe',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 24, 12, 15, 51, 534357)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 24, 12, 15, 51, 510909)),
        ),
    ]
