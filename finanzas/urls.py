from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    path('agregar/', views.agregar_transaccion, name='agregar_transaccion'),
]