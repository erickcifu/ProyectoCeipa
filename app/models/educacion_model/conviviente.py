from django.db import models
from app.models.educacion_model.parentesco import Parentesco
from app.models.educacion_model.vivienda import vivienda

class Conviviente(models.Model):
    vivienda = models.ForeignKey(vivienda, on_delete=models.CASCADE)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE)

    nombres_conviviente = models.CharField(max_length=50,null=False )
    apellidos_conviviente = models.CharField(max_length=100,null=True)
    estado_conviviente = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()

    def delete(self, *args):
        self.estado_conviviente = False
        self.save()
        return True