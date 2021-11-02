from django.db import models

from .persona_basica import PersonaBasica
from .tipo_emprendimiento import TipoEmp
from app.models.educacion_model.municipioModel import municipio


class Emprendimiento(models.Model):
    nombres_emp = models.CharField(max_length=255)
    Monto_Capital = models.IntegerField()
    fecha_inicio = models.DateField()

    persona = models.ForeignKey(PersonaBasica, on_delete=models.CASCADE, related_name="Em_Persona")
    Tipoemp = models.ForeignKey(TipoEmp, on_delete=models.CASCADE, related_name="Em_tipoemp")
    direccion_exacta = models.CharField(max_length=255, null=True, blank=True)
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="Em_muni")
    estado_Emprendimiento = models.BooleanField(default=True)
    emprendimiento_proceso = models.BooleanField(default=False)

    def __str__(self):
        return self.nombres_emp

    def delete(self, *args):
        self.estado_Emprendimiento = False
        self.save()
        return True
