from django.db import models
class Etapa(models.Model):
    nombre_etapa = models.CharField(max_length=100)
    estado_etapa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_etapa

    def delete(self, *args):
        self.estado_etapa = False
        self.save()
        return True
