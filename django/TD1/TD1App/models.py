
from typing import Type
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

class Compte (models.Model):

    CHOI = (
        ('Technicien', ('Tecnicien')),
        ('User', ('Utilisateur')),
    )

    id_c = models.AutoField (primary_key=True, editable=False)
    nom = models.CharField (max_length=17)
    prenom = models.CharField (max_length=20)
    password = models.CharField (max_length=20)
    poste = models.CharField (max_length=15, choices=CHOI, default='User')
    email = models.EmailField (max_length=50)

class Infrastructure (models.Model):

    id_i = models.AutoField (primary_key=True, editable=False)
    entreprise = models.CharField (max_length=30)
    responsable = models.CharField (max_length=17)
    Entretien = models.DateField (default= datetime.now())
    departement = models.CharField (max_length=40)

class Equipement (models.Model):

    CHOIX = (
        ('Ordinateur', ('Ordinateur')),
        ('Serveur', ('Serveur')),
        ('Switch', ('Commutateur')),
        ('Routeur', ('Router')),
    )

    id_e = models.AutoField (primary_key=True, editable=False)
    Type = models.CharField (max_length=15, choices=CHOIX, default='Ordinateur')
    infra = models.CharField (max_length=30)
    user = models.CharField (max_length=17)
    maj = models.DateField (default = datetime.now())