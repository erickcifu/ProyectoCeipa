from django.db import models

class Tipo_medio(models.Model):
    tipo_medio = models.CharField(max_length=55)
    estado_tmedio = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_medio

    def delete(self, *args):
        self.estado_tmedio = False
        self.save()
        return True
