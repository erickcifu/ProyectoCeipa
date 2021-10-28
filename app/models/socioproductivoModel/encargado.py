from django.db import models

from app.models.educacion_model.parentesco import Parentesco
from .ocupacionTutor import OcupacionTutor


class Encargado(models.Model):
    nombres_encar = models.CharField(max_length=255)
    apellidos_encar = models.CharField(max_length=255)
    fecha_nacimientoE = models.DateField()
    TelefonoE = models.CharField(max_length=8)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE, related_name="E_Parentesco")
    octutor = models.ForeignKey(OcupacionTutor, on_delete=models.CASCADE, related_name="E_OcupacionTutor")
    estado_Encargado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres_encar

    def delete(self, *args):
        self.estado_Encargado = False
        self.save()
        return True
