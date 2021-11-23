from django.db import models
from .persona import Persona
from .CarGrup import CargoGrupo
from .Gorganizado import GOrganizado
from .programaC import ProgramaC

class LiderComunitario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="B_personaM")
    cargo_grupo = models.ForeignKey(CargoGrupo, on_delete=models.CASCADE, related_name="C_cargoGM")
    grupo_orga = models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="G_organizado")
    programa_c = models.ForeignKey(ProgramaC, on_delete=models.CASCADE, related_name="P_ceipa", null=True, blank=True)
    leer_l = models.BooleanField(default=False)
    escribir_l = models.BooleanField(default=False)
    vacuna_covid_l = models.BooleanField(default=False)
    periodo = models.CharField(max_length=50,null=True, blank=True)
    fecha_inicio_l = models.DateField()
    fecha_fin_l = models.DateField()
    correo_lideres = models.EmailField(max_length=150, null=True, blank=True)
    estado_liders = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado = False
        self.save()
        return True
