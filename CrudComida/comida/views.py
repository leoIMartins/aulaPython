from django.shortcuts import render, redirect
from comida.models import Comida
from comida.forms import ComidaForm


def list_comida(request):
    comidas = Comida.objects.all()
    return render(request, 'comida.html', {'comidas': comidas})


def create_comida(request):
    form = ComidaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_comida')

    return render(request, 'agenda-form.html', {'form': form})


def update_comida(request, id):
    comida = Comida.objects.get(id=id)
    form = ComidaForm(request.POST or None, instance=comida)

    if form.is_valid():
        form.save()
        return redirect('list_comida')

    return render(request, 'comida-form.html', {'form': form, 'comida': comida})


def delete_comida(request, id):
    comida = Comida.objects.get(id=id)

    if request.method == 'POST':
        comida.delete()
        return redirect('list_comida')

    return render(request, 'comida-delete-confirm.html', {'comida': comida})