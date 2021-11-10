from django.db import models

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=100, unique=True, verbose_name='rol')
    estado_rol = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nombre_rol

