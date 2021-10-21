from django.db import models
from app.models.educacion_model.grados import grados

class EstudiosAnt(models.Model):
    grado =models.ForeignKey(grados, on_delete=models.CASCADE, related_name="E_grado")
    nombre_establecimiento = models.CharField(max_length=100,null=False)
    repitente= models.BooleanField(default=True)
    telefono = models.CharField(max_length=8)
    apoyo_ong = models.BooleanField(default=False)
    nombre_ong = models.CharField(max_length=100, null=True, blank=True)
    estado_estudiosant = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_establecimiento

    def delete(self, *args):
            self.estado_estudiosant = False
            self.save()
            return True
