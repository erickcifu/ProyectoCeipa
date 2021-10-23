from django.db import models

class PadresSociop(models.Model):
    nombre_madre = models.CharField(max_length=100, null=True, blank=True)
    telefono_madre = models.CharField(max_length=8, null=True, blank=True)
    ocupacion_madre = models.CharField(max_length=150, null=True, blank=True)
    nombre_padre = models.CharField(max_length=100, null=True, blank=True)
    telefono_padre = models.CharField(max_length=8, null=True, blank=True)
    ocupacion_padre = models.CharField(max_length=150, null=True, blank=True)
    estado_padres = models.BooleanField(default=True)

    def __str__(self):
        if self.nombre_madre:
            return self.nombre_madre
        elif self.nombre_padre:
            return self.nombre_padre
        else:
            return 'Sin datos'

    def delete(self, *args):
        self.estado_padres = False
        self.save()
        return True
