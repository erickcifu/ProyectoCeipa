from django.db import models
from .tutor_muni import TutorMuni
from .persona import Persona
from app.models.educacion_model.ocupacion import ocupacion
from .establecimiento import Establecimiento

class Beneficiado(models.Model):
    tutor = models.ForeignKey(TutorMuni, on_delete=models.CASCADE, related_name="B_tutor")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="B_persona")
    fecha_nacimiento_benef = models.DateField()
    ocup = models.ForeignKey(ocupacion, on_delete=models.CASCADE, related_name="B_ocupacion")
    establecimiento = models.CharField(max_length=100, null=True, blank=True)
    establecimiento_privado = models.BooleanField(default=False)
    establecimiento_publico = models.BooleanField(default=False)
    nivel_primario = models.BooleanField(default=False)
    nivel_secundario = models.BooleanField(default=False)
    nivel_universitario = models.BooleanField(default=False)
    estado_beneficiado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)

    def delete(self, *args):
        self.estado_beneficiado = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
