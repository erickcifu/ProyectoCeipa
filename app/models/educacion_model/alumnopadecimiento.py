from django.db import models
from app.models.educacion_model.padecimientoModel import Padecimiento
from app.models.educacion_model.alumnoModelo import Alumno

class Apadecimiento(models.Model):
    padecimiento = models.ForeignKey(Padecimiento, on_delete=models.CASCADE, related_name="A_padecimiento", null=True)
    alumno =models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="P_alumno", null=True)
    tratamiento = models.CharField(max_length=205,null=False)
    lugar = models.CharField(max_length=205,null=False)
    estado_Alpadecimiento = models.BooleanField(default=True)

    def __str__(self):
        return str(self.padecimiento)

    def delete(self, *args):
        self.estado_Alpadecimiento = False
        self.save()
        return True
