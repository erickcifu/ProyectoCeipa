from django.db import models
from .persona_basica import PersonaBasica

class GastoFamiliar(models.Model):
    servicio = models.CharField(max_length=30)
    cantidad_servicio = models.CharField(max_length=100)
    gasto_persona = models.ForeignKey(PersonaBasica, on_delete=models.CASCADE, related_name="per_g")
    estado_gastofamiliar = models.BooleanField(default=True)

    def __str__(self):
        return self.servicio

    def delete(self, *args):
        self.estado_gastofamiliar = False
        self.save()
        return True
