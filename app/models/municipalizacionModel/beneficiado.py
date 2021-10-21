from django.db import models
from .tutor_muni import TutorMuni
from .persona import Persona
from app.models.educacion_model.ocupacion import ocupacion
from .establecimiento import Establecimiento

class Beneficiado(models.Model):
    tutor = models.ForeignKey(TutorMuni, on_delete=models.CASCADE, related_name="B_tutor")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="B_persona")
    ocup = models.ForeignKey(ocupacion, on_delete=models.CASCADE, related_name="B_ocupacion")
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name="B_establecimiento")
    estado_beneficiado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)

    def delete(self, *args):
        self.estado_beneficiado = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
