from django.db import models
#from .persona import Persona
#from .cargo import Cargo
from .Gorganizado import GOrganizado
from .programaC import ProgramaC

class LiderComunitario(models.Model):
    #persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="P_persona")
    #cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="C_cargo")
    grupo_orga = models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="G_organizado")
    programa_c = models.ForeignKey(ProgramaC, on_delete=models.CASCADE, related_name="P_ceipa")
    leer = models.BooleanField(default=True)
    escribir = models.BooleanField(default=True)
    vacuna_covid = models.BooleanField(default=True)
    periodo = models.CharField(max_length=50,null=False)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado = False
        self.save()
        return True
