from django.db import models
from .tutor_muni import TutorMuni
from .persona import Persona
from app.models.educacion_model.genero import genero
from app.models.educacion_model.ocupacion import ocupacion
from app.models.educacion_model.estudiosantModel import EstudiosAnt

class Beneficiado(models.Model):
    tutor = models.ForeignKey(TutorMuni, on_delete=models.CASCADE, related_name="B_tutor")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="B_persona")
    gen = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="B_genero")
    ocup = models.ForeignKey(ocupacion, on_delete=models.CASCADE, related_name="B_ocupacion")
    estudios_anteriores = models.ForeignKey(EstudiosAnt, on_delete=models.CASCADE, related_name="B_estudios")

    estado_beneficiado = models.BooleanField(default=True)


    def delete(self, *args):
        self.estado_beneficiado = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
