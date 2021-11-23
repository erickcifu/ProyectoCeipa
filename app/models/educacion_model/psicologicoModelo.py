from django.db import models
from app.models.educacion_model.alumnoModelo import Alumno

class psicologico(models.Model):
    alumno =models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="A_alumno")
    Analisis_psicologico = models.CharField(max_length=255,null=False )
    tratamiento = models.CharField(max_length=255, null=True, blank=True)
    fecha_Analisis = models.DateField()
    Entrevistador = models.CharField(max_length=255, null=True, blank=True)
    tiene_sueños = models.BooleanField(default=False)
    sueños = models.CharField(max_length=255, null=True, blank=True)
    estado_psicologico = models.BooleanField(default=True)

    def __str__(self):
        return self.Analisis_psicologico

    def delete(self, *args):
        self.estado_psicologico = False
        self.save()
        return True
