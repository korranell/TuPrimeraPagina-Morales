from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    image = models.ImageField(upload_to='imagen/', null=True, blank=True)

    def __str__(self):
        return f"{self.username}"  