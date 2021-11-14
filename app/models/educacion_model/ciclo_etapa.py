from django.db import models
from .etapa import Etapa
from .ciclo import Ciclo

class Ciclo_etapa(models.Model):
    c_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, related_name="ce_etapa")
    ciclo_c = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="ce_ciclo")
    estado_ce = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ciclo_c)

    def delete(self, *args):
        self.estado_ce = False
        self.save()
        return True
