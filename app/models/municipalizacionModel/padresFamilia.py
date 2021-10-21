from django.db import models
from .persona import Persona
from .programaC import ProgramaC
from .Gorganizado import GOrganizado
from .CarGrup import CargoGrupo

class PadresFamilia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="per_padre")
    leer = models.BooleanField(default=False)
    escribir = models.BooleanField(default=False)
    cantidad_hijos = models.IntegerField()
    vacunaCovid = models.BooleanField(default=False)
    participacionG = models.BooleanField(default=False)
    grupo = models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="grupoOr_padre", null=True, blank=True)
    cargo = models.ForeignKey(CargoGrupo, on_delete=models.CASCADE, related_name="cargoG_padre", null=True, blank=True)
    programaC = models.ForeignKey(ProgramaC, on_delete=models.CASCADE, related_name="programa_padre", null=True, blank=True)
    estado_padres = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)

    def delete(self, *args):
        self.estado_padres = False
        self.save()
        return True
