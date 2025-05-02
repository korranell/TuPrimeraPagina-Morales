from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings

class Transaccion(models.Model):
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, blank=True, null=True)  # Nueva categoría
    imagen = models.ImageField(upload_to='transacciones/', null=True, blank=True)

    def __str__(self):
        return f"{self.descripcion} - {self.monto} - {self.fecha}"