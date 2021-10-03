from django.db import models
from .persona import Persona
from app.models.educacion_model.padecimientoModel import Padecimiento
class PadPer(models.Model):
    medicamentos = models.CharField(max_length=255,null=False)
    observacion = models.CharField(max_length=255,null=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="PP_persona")
    padecimiento = models.ForeignKey(Padecimiento, on_delete=models.CASCADE, related_name="PP_padecimiento")
    estado_padper = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_padper = False
        self.save()
        return True
