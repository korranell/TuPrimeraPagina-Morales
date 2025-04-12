from django.shortcuts import render, redirect
from .models import Categoria, Transaccion
from .forms import TransaccionForm

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

