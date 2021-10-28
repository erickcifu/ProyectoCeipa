from django.db import models
from .persona_basica import PersonaBasica

class InfoEconomica(models.Model):
    pariente = models.CharField(max_length=100)
    cantidad_mensual = models.FloatField(null=True, blank=True)
    procedencia_ingreso = models.CharField(max_length=100, null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    eco_persona = models.ForeignKey(PersonaBasica, on_delete=models.CASCADE, related_name="info_pers")
    estado_infoeco = models.BooleanField(default=True)

    def __str__(self):
        return self.pariente

    def delete(self, *args):
        self.estado_infoeco = False
        self.save()
        return True
