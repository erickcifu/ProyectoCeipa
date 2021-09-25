from django.db import models

#from .area import Area
#from .beneficiado import Beneficiado

class AusenBeneficiado(models.Model):
    #area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="A_area")
    #beneficiado = models.ForeignKey(Beneficiado, on_delete=models.CASCADE, related_name="B_beneficiado")
    observaciones = models.CharField(max_length=100,null=False)
    fecha = models.DateField()
    estado = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado = False
        self.save()
        return True