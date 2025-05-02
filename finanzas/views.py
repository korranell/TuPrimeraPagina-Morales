from django.db.models import Q
from .models import Transaccion
from .forms import TransaccionForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import UpdateView
from .models import Transaccion
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Transaccion
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

@login_required
def agregar_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            transaccion = form.save(commit=False)
            transaccion.usuario = request.user
            transaccion.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm()
    return render(request, 'agregar_transaccion.html', {'form': form})

def lista_transacciones(request):
    query = request.GET.get('q', '')
    if query:
        transacciones = Transaccion.objects.filter(Q(descripcion__icontains=query))
    else:
        transacciones = Transaccion.objects.all()
    return render(request, 'finanzas/lista_transacciones.html', {'transacciones': transacciones})

class DetalleTransaccion(DetailView):
        model = Transaccion
        template_name = 'finanzas/detalle_transaccion.html'
        context_object_name = 'transaccion'

class ModificarTransaccion(UpdateView):
        model = Transaccion
        fields = ['descripcion', 'monto', 'categoria', 'imagen']  
        template_name = 'finanzas/modificar_transaccion.html'
        context_object_name = 'transaccion'
        success_url = reverse_lazy('lista_transacciones')


class EliminarTransaccion(DeleteView):
        model = Transaccion
        template_name = 'finanzas/eliminar_transaccion.html'
        context_object_name = 'transaccion'
        success_url = reverse_lazy('lista_transacciones')
