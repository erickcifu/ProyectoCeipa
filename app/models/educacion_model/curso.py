from django.db import models
from .grado import Grado

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100, null=False)
    descripcion_curso = models.CharField(max_length=255)
    grado = models.Foreignkey(Grado, on_delete=models.CASCADE, related_name="curso_grado")
    estado_curso = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_curso = False
        self.save()
        return True