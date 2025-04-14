from django.shortcuts import render, redirect
from .models import Categoria, Transaccion
from .forms import TransaccionForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


@login_required
def lista_transacciones(request):
    ...

def index(request):
    categorias = Categoria.objects.all()
    transacciones = Transaccion.objects.all()
    return render(request, "finanzas/index.html", {"categorias": categorias, "transacciones": transacciones})

def agregar_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')  # Redirigir a la lista de transacciones después de guardar
    else:
        form = TransaccionForm()
    return render(request, 'finanzas/nueva_transaccion.html', {'form': form})

def lista_transacciones(request):
    transacciones = Transaccion.objects.all()  
    return render(request, 'finanzas/lista_transacciones.html', {'transacciones': transacciones})

def lista_transacciones(request):
    query = request.GET.get('q')  # Toma el texto de búsqueda
    if query:
        transacciones = Transaccion.objects.filter(
            Q(descripcion__icontains=query) |
            Q(categoria__nombre__icontains=query)
        )
    else:
        transacciones = Transaccion.objects.all()
    
    return render(request, 'finanzas/lista_transacciones.html', {
        'transacciones': transacciones,
        'query': query
    })

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