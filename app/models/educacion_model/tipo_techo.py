from django.db import models

class Tipo_techo(models.Model):
    tipo_techo = models.CharField(max_length=50, null=False)
    descripcion_techo = models.CharField(max_length=100,null=True, blank=True)
    estado_techo = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_techo

    def delete(self, *args):
        self.estado_techo = False
        self.save()
        return True
