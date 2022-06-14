# Generated by Django 4.0.3 on 2022-06-13 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TD1App', '0014_infrastructure_departement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='Date_DE_NAISSANCE',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 49, 772586)),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='maj',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 49, 773590)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='Entretien',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 49, 773265)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='departement',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 49, 749583)),
        ),
    ]
