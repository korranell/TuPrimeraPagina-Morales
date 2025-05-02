from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import DetalleTransaccion


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    path('agregar/', views.agregar_transaccion, name='agregar_transaccion'),
    path('transaccion/<int:pk>/', DetalleTransaccion.as_view(), name='detalle_transaccion'),
    path('modificar/<int:pk>/', views.ModificarTransaccion.as_view(), name='modificar_transaccion'),
    path('eliminar/<int:pk>/', views.EliminarTransaccion.as_view(), name='eliminar_transaccion'),
]

