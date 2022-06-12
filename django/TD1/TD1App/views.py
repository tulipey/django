from turtle import pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from TD1App.models import Machine, Employe
from TD1App.forms import AddMachineForm, AddEmployeForm

def index(request):
	context = {}
	return render(request, 'index.html', context)

def machine_list_view(request):
    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'td1app/machine_list.html', context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk)
	context = {'machine': machine}
	return render(request, 'td1app/machine_detail.html', context)

def employe_list_view(request):
    employes = Employe.objects.all()
    context = {'employes': employes}
    return render(request, 'td1app/employe_list.html', context)

def employe_detail_view(request, pk):
	employe = get_object_or_404(Employe, id=pk)
	context = {'employe': employe}
	return render(request, 'td1app/employe_detail.html', context)

def machine_add_from(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else :
        form = AddMachineForm()
        context = {'form': form}
        return render(request, 'td1app/machine_add.html', context)

def employe_add_from(request):
    if request.method == 'POST':
        form = AddEmployeForm(request.POST or None)
        if form.is_valid():
            new_machine = Employe(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('employes')
    else :
        form = AddEmployeForm()
        context = {'form': form}
        return render(request, 'td1app/employe_add.html', context)