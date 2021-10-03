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
    estado_maestro = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_maestro = False
        self.save()
        return True
