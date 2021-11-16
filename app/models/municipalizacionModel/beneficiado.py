from django.db import models
from .tutor_muni import TutorMuni
from .persona import Persona
from app.models.educacion_model.ocupacion import ocupacion

class Beneficiado(models.Model):
    tutor = models.ForeignKey(TutorMuni, on_delete=models.CASCADE, related_name="B_tutor")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="B_persona")
    fecha_nacimiento_benef = models.DateField()
    trabaja_benef = models.BooleanField(default=False)
    ocup = models.ForeignKey(ocupacion, on_delete=models.CASCADE, related_name="B_ocupacion", null=True, blank=True)
    establecimiento = models.CharField(max_length=100, null=True, blank=True)
    establecimiento_privado = models.BooleanField(default=False)
    establecimiento_publico = models.BooleanField(default=False)
    nivel_primario = models.BooleanField(default=False)
    nivel_secundario = models.BooleanField(default=False)
    nivel_universitario = models.BooleanField(default=False)
    toma_medicamento = models.BooleanField(default=False)
    estado_beneficiado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona)

    def delete(self, *args):
        self.estado_beneficiado = False
        self.save()
        return True
