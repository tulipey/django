from django import forms
from django.forms import ValidationError
from TD1App.models import Machine, Employe


class createMachineFrom(forms.Form):
    nom = forms.CharField(label="Nom de la machine")
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 6:
            raise ValidationError(("Erreur de format pour le champ 'nom'"))
        return data

class AddMachineForm(forms.Form):

    nom = forms.CharField(required=True, label='nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data)> 32:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

class AddEmployeForm(forms.Form):

    nom = forms.CharField(required=True, label='nom employé')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

class AddInfrastructureForm(forms.Form):

    nom = forms.CharField(required=True, label="nom d'infrastructure")

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data