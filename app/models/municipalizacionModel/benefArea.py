from django.db import models
from .programaC import ProgramaC
from .beneficiado import Beneficiado
from .area import Area

class BeneficiadoArea(models.Model):
    area = models.ForeginKey(Area, on_delete=models.CASCADE, related_name="ba_Area")
    programa = models.ForeginKey(ProgramaC, on_delete=models.CASCADE, related_name="ba_programaC")
    beneficiado = models.ForeginKey(Beneficiado, on_delete=models.CASCADE, related_name="ba_benef")
    observacion = models.CharField(max_length=250, null=True, blank=True)
    fecha = models.DateField()
    estado_ba = models.BooleanField(default=True)

    def __str__(self):
        return str(self.area)

    def delete(self, *args):
        self.estado_ba = False
        self.save()
        return True
