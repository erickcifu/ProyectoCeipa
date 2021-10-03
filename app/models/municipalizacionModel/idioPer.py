from django.db import models
from app.models.educacion_model.idioma import idioma
from .persona import Persona

class IdiomaPersona(models.Model):
    idioma= models.ForeignKey(idioma, on_delete=models.CASCADE, related_name="P_idioma")
    persona= models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="I_persona")
    estado_ip = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_ip = False
        self.save()
        return True
