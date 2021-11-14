from django.db import models
from .alumnoModelo import Alumno

class AspectosLab(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="aspect_alumn")
    empleador = models.CharField(max_length=100, null=True, blank=True)
    tel_empleador = models.CharField(max_length=8, null=True, blank=True)
    area_trabaja = models.CharField(max_length=100, null=True, blank=True)
    jornada = models.CharField(max_length=100, null=True, blank=True)
    dias_trabajo = models.PositiveIntegerField(null=True, blank=True)
    hora_entrada = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    hora_salida = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    i_diario = models.BooleanField(default=False)
    i_semanal = models.BooleanField(default=False)
    i_quincenal = models.BooleanField(default=False)
    i_mensual = models.BooleanField(default=False)
    total_ingreso = models.FloatField(null=True, blank=True)
    destino_ingreso = models.CharField(max_length=255, null=True, blank=True)
    edad_inicio_trabajo = models.PositiveIntegerField(null=True, blank=True)
    familia_migrante = models.BooleanField(default=True)
    cantidad_familiares = models.CharField(max_length=10, null=True, blank=True)
    estado_laborales = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ocup)

    def delete(self, *args):
            self.estado_laborales = False
            self.save()
            return True
