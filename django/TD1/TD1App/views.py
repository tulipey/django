from turtle import pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from TD1App.models import Infrastructure, Equipement, Compte
from TD1App.forms import AddEquipementForm, AddInfrastructureForm, AddCompteForm

def index(request):
	context = {}
	return render(request, 'index.html', context)

# Infrastructure

def infrastructure_list_view(request):
    infrastructures = Infrastructure.objects.all()
    context = {'infrastructures': infrastructures}
    return render(request, 'td1app/infrastructure_list.html', context)

def infrastructure_detail_view(request, pk):
	infrastructure = get_object_or_404(Infrastructure, id_i=pk)
	context = {'infrastructure': infrastructure}
	return render(request, 'td1app/infrastructure_detail.html', context)

def infrastructure_add_from(request):
    if request.method == 'POST':
        form = AddInfrastructureForm(request.POST or None)
        if form.is_valid():
            new_infrastructure = Infrastructure(entreprise=form.cleaned_data['entreprise'])
            new_infrastructure.save()
            return redirect('infrastructures')
    else :
        form = AddInfrastructureForm()
        context = {'form': form}
        return render(request, 'td1app/infrastructure_add.html', context)

# Equipement

def equipement_list_view(request):
    equipements = Equipement.objects.all(id_i=pk)
    context = {'equipement': equipements}
    return render(request, 'td1app/infrastructure_detail.html', context)

def equipement_add_from(request):
    if request.method == 'POST':
        form = AddEquipementForm(request.POST or None)
        if form.is_valid():
            new_machine = Equipement(infrastructure=form.cleaned_data['infra'])
            new_machine.save()
            return redirect('infrastructures')
    else :
        form = AddEquipementForm()
        context = {'form': form}
        return render(request, 'td1app/equipement_add.html', context)