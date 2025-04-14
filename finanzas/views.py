from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Categoria, Transaccion
from .forms import TransaccionForm
from django.contrib.auth.decorators import login_required

def index(request):
    categorias = Categoria.objects.all()
    transacciones = Transaccion.objects.all()
    return render(request, "finanzas/index.html", {"categorias": categorias, "transacciones": transacciones})

@login_required
def agregar_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            transaccion.user = request.user
            transaccion.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm()
    return render(request, 'finanzas/agregar_transaccion.html', {'form': form})

def lista_transacciones(request):
    query = request.GET.get('q', '')
    if query:
        transacciones = Transaccion.objects.filter(Q(descripcion__icontains=query))
    else:
        transacciones = Transaccion.objects.all()
    return render(request, 'finanzas/lista_transacciones.html', {'transacciones': transacciones})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_transacciones')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})