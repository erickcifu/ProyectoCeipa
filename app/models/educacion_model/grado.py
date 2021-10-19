from django.db import models

class Grado(models.Model):
    nombre_grado = models.CharField(max_length=50,null=False )
    descripcion_grado = models.CharField(max_length=255, null=True, blank=True)
    estado_grado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_grado

    def delete(self, *args):
        self.estado_grado = False
        self.save()
        return True
