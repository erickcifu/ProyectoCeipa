from django.db import models

class Establecimiento(models.Model):
    nombre_establecimiento = models.CharField(max_length=50,null=False)
    direccion = models.CharField(max_length=80)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_establecimiento

    def delete(self, *args):
        self.estado = False
        self.save()
        return True
