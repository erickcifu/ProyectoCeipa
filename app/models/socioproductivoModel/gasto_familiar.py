from django.db import models

class GastoFamiliar(models.Model):
    servicio = models.CharField(max_length=30)
    cantidad_servicio = models.CharField(max_length=100)
    estado_gastofamiliar = models.BooleanField(default=True)

    def __str__(self):
        return self.servicio

    def delete(self, *args):
        self.estado_gastofamiliar = False
        self.save()
        return True
