from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField()
    categoria = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        if self.usuario:
            return f"Transacción de {self.usuario.username}"
        else:
            return "Transacción sin usuario"
    
