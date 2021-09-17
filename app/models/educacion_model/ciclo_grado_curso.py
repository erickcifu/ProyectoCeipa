from django.db import models
from .personalEducativo import personalEducativo
from .curso import Curso
from .ciclo_grado import Ciclo_grado

class Ciclo_grado_curso(models.Model):
    maestro= models.Foreignkey(personalEducativo, on_delete=models.CASCADE, related_name="cgc_personal")
    curso = models.Foreignkey(Curso, on_delete=models.CASCADE, related_name="cgc_curso)
    ciclo_grado = models.Foreignkey(Ciclo_grado, on_delete=models.CASCADE, related_name="cgc_cg")
    estado_cgc = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_cgc = False
        self.save()
        return True
