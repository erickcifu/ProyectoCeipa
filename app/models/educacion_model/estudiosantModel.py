from django.db import models
from .grado import Grado

class EstudiosAnt(models.Model):
    grado =models.ForeignKey(Grado, on_delete=models.CASCADE, related_name="E_grado", null=True, blank=True)
    nombre_establecimiento = models.CharField(max_length=100,null=True, blank=True)
    repitente= models.BooleanField(default=False)
    telefono = models.CharField(max_length=8, null=True, blank=True)
    apoyo_ong = models.BooleanField(default=False)
    nombre_ong = models.CharField(max_length=100, null=True, blank=True)
    estado_estudiosant = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_establecimiento

    def delete(self, *args):
            self.estado_estudiosant = False
            self.save()
            return True
