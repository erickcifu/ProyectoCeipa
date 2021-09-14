from django.db import models
from .tarea import tarea

class tarea_alumno(models.Model):
    tarea = models.Foreignkey(tarea, on_delete=models.CASCADE, related_name="ta_tarea")
    #Foreignkey alumno
    nota_obtenida = models.FloatField()
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    estado_tareaAlumno = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_tareaAlumno = False
        self.save()
        return True
