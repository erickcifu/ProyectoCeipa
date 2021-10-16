from django.db import models
from .establecimiento import Establecimiento
from .persona import Persona
from .CarGrup import CargoGrupo
from .Gorganizado import GOrganizado

class Maestro(models.Model):
    establecimiento= models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name="M_Est")
    persona= models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="M_persona")
    gruporg= models.ForeignKey(CargoGrupo, on_delete=models.CASCADE, related_name="M_grupOrg")
    cargogrup= models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="M_cargoG")
    vacuna_covid = models.BooleanField(default=True)
    Renas = models.BooleanField(default=True)
    Pargrupo = models.BooleanField(default=True)
    estado_maestro = models.BooleanField(default=True)

    def __str__(self):
        return self.persona

    def delete(self, *args):
        self.estado_maestro = False
        self.save()
        return True
