# Generated by Django 4.0.3 on 2022-06-13 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TD1App', '0013_alter_employe_date_de_naissance_alter_equipement_maj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructure',
            name='departement',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='Date_DE_NAISSANCE',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 34, 309369)),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='maj',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 34, 310281)),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='Entretien',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 34, 309986)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 22, 55, 34, 286671)),
        ),
    ]
