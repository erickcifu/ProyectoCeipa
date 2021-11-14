from django.db import models
from .persona import Persona
from .tipo_medio import Tipo_medio

class MedioComuni(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="P_personaM")
    nombre_medio = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100, null=True, blank=True)
    t_medio = models.ForeignKey(Tipo_medio, on_delete=models.CASCADE, related_name="tipo_med")
    correo_medio = models.EmailField(max_length=55, null=True, blank=True)
    vacuna_medio = models.BooleanField(default=False)
    telefono_medio = models.CharField(max_length=8)
    estado = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado = False
        self.save()
        return True
