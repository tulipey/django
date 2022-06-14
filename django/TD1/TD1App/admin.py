from django.contrib import admin
from .models import Compte, Infrastructure, Equipement

admin.site.register(Infrastructure)
admin.site.register(Equipement)
admin.site.register(Compte)