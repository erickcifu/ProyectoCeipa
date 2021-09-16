from django.db import models
from .personalEducativo import personalEducativo

class tarea(models.Model):
    titulo_tarea = models.CharField(max_length=50,null=False )
    descripcion_tarea = models.CharField(max_length=255, null=True, blank=True)
    maestro = models.Foreignkey(personalEducativo, on_delete=CASCADE, related_name="tarea_maestro")
    #Foreignkey de ciclo_grado_curso
    nota_tarea = models.FloatField()
    fecha_entrega = models.DateTimeField()
    estado_tarea = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_tarea = False
        self.save()
        return True
