from django.urls import path
from .views import registro, profile, editar
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('profile/', profile, name='profile'),
    path('editar/', editar, name='editar'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]