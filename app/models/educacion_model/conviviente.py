from django.db import models
from .parentesco import Parentesco
from .vivienda import vivienda

class Conviviente(models.Model):
    vivienda = models.ForeignKey(vivienda, on_delete=models.CASCADE, related_name="V_vivienda")
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE, related_name="P_parentesco")

    nombres_conviviente = models.CharField(max_length=50,null=False)
    apellidos_conviviente = models.CharField(max_length=100,null=True)
    estado_conviviente = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombres_conviviente

    def delete(self, *args):
        self.estado_conviviente = False
        self.save()
        return True
