from django.db import models
from .grado import Grado
from .ciclo import Ciclo
from .seccionModelo import seccion

class Ciclo_grado(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name="cg_grado")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="cg_ciclo")
    seccion = models.ForeignKey(seccion, on_delete=models.CASCADE, related_name="cg_seccion")
    estado_cg = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ciclo)

    def delete(self, *args):
        self.estado_cg = False
        self.save()
        return True
