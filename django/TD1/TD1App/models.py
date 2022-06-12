from django.db import models
from datetime import datetime

class Machine (models.Model):

    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Server - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField (primary_key=True, editable=False)
    nom = models.CharField (max_length=6)
    maintenanceDate = models.DateField (default = datetime.now())
    mach = models.CharField (max_length=32, choices=TYPE, default='PC')

class Employe (models.Model):

    TYPE = (
        ('Technicien', ('ITACHI')),
        ('Directeur', ('Aime sa famille et l argent')),
        ('PDG', ('Aime l argent')),
    )

    id = models.AutoField (primary_key=True, editable=False)
    nom = models.CharField (max_length=35)
    Date_DE_NAISSANCE = models.DateField (default = datetime.now())
    mach = models.CharField (max_length=32, choices=TYPE, default='Technicien')