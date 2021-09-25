from django.db import models
from .personalEducativo import personalEducativo
from .ciclo_grado_curso import Ciclo_grado_curso

class tarea(models.Model):
    titulo_tarea = models.CharField(max_length=50,null=False )
    descripcion_tarea = models.CharField(max_length=255, null=True, blank=True)
    maestro = models.ForeignKey(personalEducativo, on_delete=models.CASCADE, related_name="tarea_maestro")
    ciclo_grado_curso = models.ForeignKey(Ciclo_grado_curso, on_delete=models.CASCADE,related_name="cgc_tarea")
    nota_tarea = models.FloatField()
    fecha_entrega = models.DateTimeField()
    estado_tarea = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo_tarea

    def delete(self, *args):
        self.estado_tarea = False
        self.save()
        return True
