from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import registrar_usuario


urlpatterns = [
    path('', views.index, name='index'),
    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    path('agregar/', views.agregar_transaccion, name='agregar_transaccion'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrarse/', registrar_usuario, name='registrarse'),
]
