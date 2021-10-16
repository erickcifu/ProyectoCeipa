from django.db import models

class ocupacion(models.Model):
    nombre_ocupacion = models.CharField(max_length=50,null=False )
    descripcion_ocupacion = models.CharField(max_length=100,null=True, blank=True)
    estado_ocupacion = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_ocupacion

    def delete(self, *args):
        self.estado_ocupacion = False
        self.save()
        return True
