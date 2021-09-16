from django.db import models

class Ciclo(models.Model):
    anio = models.IntegerField()
    estado_ciclo = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_ciclo = False
        self.save()
        return True
