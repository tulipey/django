from django import forms
from django.forms import ValidationError
 

# Infrastructure

class AddInfrastructureForm(forms.Form):

    entreprise = forms.CharField(required=True, label="nom d'infrastructure")
    responsable = forms.CharField(required=True, label="nom du responsable")
    departement = forms.CharField(required=True, label="nom du departement")


    def clean_nom(self):
        data = self.cleaned_data["entreprise"]
        if len(data) > 32:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

# Equipement

class AddEquipementForm(forms.Form):

    infra = forms.CharField(required=True, label="nom d'infrastructure")
    user = forms.CharField(required=True, label="nom de l'utilisateur")


    def clean_nom(self):
        data = self.cleaned_data["infra"]
        if len(data) > 32:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

# Compte

class AddCompteForm(forms.Form):

    nom = forms.CharField(required=True, label="nom l'utilisateur")
    prenom = forms.CharField(required=True, label="prenom de l'utilisateur")
    email = forms.EmailField(required=True, label="email de l'utilisateur")


    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 32:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data