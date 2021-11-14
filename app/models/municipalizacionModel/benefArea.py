from django.db import models
from .programaC import ProgramaC
from .beneficiado import Beneficiado
from .area import Area

class BeneficiadoArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="ba_Area")
    programa = models.ForeignKey(ProgramaC, on_delete=models.CASCADE, related_name="ba_programaC")
    beneficiado = models.ForeignKey(Beneficiado, on_delete=models.CASCADE, related_name="ba_benef")
    observacion = models.CharField(max_length=250, null=True, blank=True)
    fecha_ba = models.DateField(null=True, blank=True)
    estado_ba = models.BooleanField(default=True)

    def __str__(self):
        return str(self.area)

    def delete(self, *args):
        self.estado_ba = False
        self.save()
        return True
