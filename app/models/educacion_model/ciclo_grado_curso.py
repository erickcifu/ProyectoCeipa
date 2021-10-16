from django.db import models
from .personalEducativo import personalEducativo
from .curso import Curso
from .ciclo_grado import Ciclo_grado

class Ciclo_grado_curso(models.Model):
    maestro= models.ForeignKey(personalEducativo, on_delete=models.CASCADE, related_name="cgc_personal")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="cgc_curso")
    ciclo_grado = models.ForeignKey(Ciclo_grado, on_delete=models.CASCADE, related_name="cgc_cg")
    estado_cgc = models.BooleanField(default=True)

    def __str__(self):
        return str(self.curso)

    def delete(self, *args):
        self.estado_cgc = False
        self.save()
        return True
