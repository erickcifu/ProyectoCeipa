from django.db import models

class centro_educativo(models.Model):
    nombre_centro = models.CharField(max_length=100, null=False)
    direccion_centro = models.CharField(max_length=255, null=True, blank=True)
    codigo_centro = models.CharField(max_length=50, null=False)
    estado_centro = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_centro

    def delete(self, *args):
        self.estado_centro = False
        self.save()
        return True
