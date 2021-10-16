from django.db import models
from .persona import Persona
from .institucion import Institucion

class ComisionNA(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="comision_pers")
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="insti_comision")
    participacion = models.BooleanField(default=False)
    estado_comision = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)

    def delete(self, *args):
        self.estado_comision = False
        self.save()
        return True
