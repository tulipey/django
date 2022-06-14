from django.contrib import admin
from .models import Infrastructure, Machine, Employe

admin.site.register(Machine)
admin.site.register(Employe)
admin.site.register(Infrastructure)
