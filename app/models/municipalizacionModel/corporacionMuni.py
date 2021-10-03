from django.db import models
from .persona import Persona
from .profesion import Profesion
from .comision import Comision
from .partidopolitic import PartidoPolitic
from .CarGrup import CargoGrupo
from .Gorganizado import GOrganizado

class CorporacionMunicipal(models.Model):
    persona = models.ForeginKey(Persona, on_delete=models.CASCADE, related_name="pers_comision")
    comision = models.ForeginKey(Comision, on_delete=mmodels.CASCADE, related_name="com_cm")
    partido = models.ForeginKey(PartidoPolitic, on_delete=models.CASCADE, related_name="partidop_cm")
    participacion = models.BooleanField(default=False)
    grupo = models.ForeginKey(GOrganizado, on_delete=models.CASCADE, related_name="grupoO_cm")
    cargo = models.ForeginKey(CargoGrupo, on_delete=models.CASCADE, related_name="cargoG_cm")
    vacuna = models.BooleanField(default=False)
    estado_corporacion = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)

    def delete(self, *args):
        self.estado_corporacion = False
        self.save()
        return True
