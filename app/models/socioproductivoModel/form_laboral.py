from django.db import models
from .persona_basica import PersonaBasica

class FormacionLab(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin_formacion = models.DateField()
    persona_formacion = models.ForeignKey(PersonaBasica, on_delete=models.CASCADE, related_name="form_Persona")
    horas_formacion = models.PositiveIntegerField(null=True, blank=True)
    estado_formación = models.BooleanField(default=True)
    formacion_completada = models.BooleanField(default=False)

    def __str__(self):
        return str(self.persona_formacion)

    def delete(self, *args):
        self.estado_formación = False
        self.save()
        return True
