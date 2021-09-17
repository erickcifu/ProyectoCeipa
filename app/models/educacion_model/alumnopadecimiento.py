from django.db import models
from app.models.educacion_model.padecimientoModel import Padecimiento

class Apadecimiento(models.Model):
     padecimiento = models.ForeignKey(Padecimiento, on_delete=models.CASCADE, related_name="A_padecimiento")
     tratamiento = models.CharField(max_length=205,null=False )
     lugar = models.CharField(max_length=205,null=False )
     estado_Alpadecimiento = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_psicologico = False
        self.save()
        return True
