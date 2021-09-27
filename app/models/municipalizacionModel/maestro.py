from django.db import models
from app.models.municipalizacionModel.establecimiento import Establecimiento
from app.models.municipalizacionModel.persona import Persona
from app.models.municipalizacionModel.CarGrup import CargoGrupo
from app.models.municipalizacionModel.Gorganizado import GOrganizado

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
