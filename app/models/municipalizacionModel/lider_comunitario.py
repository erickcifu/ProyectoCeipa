from django.db import models
from .persona import Persona
from .CarGrup import CargoGrupo
from .Gorganizado import GOrganizado
from .programaC import ProgramaC

class LiderComunitario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="B_personaM")
    cargo_grupo = models.ForeignKey(CargoGrupo, on_delete=models.CASCADE, related_name="C_cargoGM")
    grupo_orga = models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="G_organizado")
    programa_c = models.ForeignKey(ProgramaC, on_delete=models.CASCADE, related_name="P_ceipa", null=True)
    leer = models.BooleanField(default=True)
    escribir = models.BooleanField(default=True)
    vacuna_covid = models.BooleanField(default=True)
    periodo = models.CharField(max_length=50,null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    correo_lideres = models.EmailField(max_length=150, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)
        
    def delete(self, *args):
        self.estado = False
        self.save()
        return True
