from django.db import models
from app.models.educacion_model.alumnoModelo import Alumno

class psicologico(models.Model):
    alumno =models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="A_alumno"
    Analisis_psicologico = models.CharField(max_length=255,null=False )
    tratamiento = models.CharField(max_length=255, null=True, blank=True)
    fecha_Analisis = models.DateTimeField()
    Entrevistador = models.CharField(max_length=255, null=True, blank=True)
    estado_psicologico = models.BooleanField(default=True)


    def delete(self, *args):
        self.estado_psicologico = False
        self.save()
        return True
