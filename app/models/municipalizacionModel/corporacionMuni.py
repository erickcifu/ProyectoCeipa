from django.db import models
from .persona import Persona
from .profesion import Profesion
from .comision import Comision
from .partidopolitic import PartidoPolitic
from .CarGrup import CargoGrupo
from .Gorganizado import GOrganizado

class CorporacionMunicipal(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="pers_comision")
    comision = models.ForeignKey(Comision, on_delete=models.CASCADE, related_name="com_cm")
    partido = models.ForeignKey(PartidoPolitic, on_delete=models.CASCADE, related_name="partido_cm")
    partido_actual = models.ForeignKey(PartidoPolitic, on_delete=models.CASCADE, related_name="partactual_cm")
    grupo = models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="grupoO_cm", null=True, blank=True)
    cargo = models.ForeignKey(CargoGrupo, on_delete=models.CASCADE, related_name="cargoG_cm", null=True, blank=True)
    vacuna = models.BooleanField(default=False)
    correo_corporacion = models.EmailField(max_length=150, null=True, blank=True)
    participacion = models.BooleanField(default=False)
    estado_corporacion = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)

    def delete(self, *args):
        self.estado_corporacion = False
        self.save()
        return True
