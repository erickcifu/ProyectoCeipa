from django.db import models
from .grado import Grado
from .ciclo import Ciclo
from .seccionModelo import seccion

class Curso(models.Model):
    grado = models.Foreignkey(Grado, on_delete=models.CASCADE, related_name="cg_grado")
    ciclo = models.Foreignkey(Ciclo, on_delete=models.CASCADE, related_name="cg_ciclo")
    seccion = models.Foreignkey(seccion, on_delete=models.CASCADE, related_name="cg_seccion")
    estado_cg = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_cg = False
        self.save()
        return True
