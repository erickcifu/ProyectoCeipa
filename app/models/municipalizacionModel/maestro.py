from django.db import models
from .persona import Persona
from .CarGrup import CargoGrupo
from .Gorganizado import GOrganizado

class Maestro(models.Model):
    establecimiento= models.CharField(max_length=255, blank=True, null=True)
    area_rural = models.BooleanField(default=False)
    area_urbana = models.BooleanField(default=False)
    est_publico = models.BooleanField(default=False)
    est_privado = models.BooleanField(default=False)
    participa_maestro = models.BooleanField(default=False)
    correo_maestro = models.EmailField(max_length=100, null=True, blank=True)
    persona_maestro = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="M_persona")
    gruporg= models.ForeignKey(CargoGrupo, on_delete=models.CASCADE, related_name="M_grupOrg", null=True, blank=True)
    cargogrup= models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="M_cargoG", null=True, blank=True)
    vacuna_covid = models.BooleanField(default=True)
    Renas = models.BooleanField(default=True)
    Pargrupo = models.BooleanField(default=True)
    estado_maestro = models.BooleanField(default=True)

    def __str__(self):
        return self.persona_maestro

    def delete(self, *args):
        self.estado_maestro = False
        self.save()
        return True
