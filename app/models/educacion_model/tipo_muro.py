from django.db import models

class Tipo_muro(models.Model):
    tipo_muro = models.CharField(max_length=50, null=False)
    descripcion_muro= models.CharField(max_length=100,null=True, blank=True)
    estado_muro = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_muro = False
        self.save()
        return True