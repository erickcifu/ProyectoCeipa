from django.db import models

class Tipo_piso (models.Model):
    tipo_piso = models.CharField(max_length=55,null=False )
    descripcion_tipopiso = models.CharField(max_length=100,null=True, blank=True)
    estado_tipopiso = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_piso

    def delete(self, *args):
        self.estado_tipopiso = False
        self.save()
        return True
