from django.db import models

class Taller(models.Model):
    nombre_taller = models.CharField(max_length=40)
    descripcion_taller = models.CharField(max_length=200)
    estado_taller = models.BooleanField(default=True)

    def __str__(self):
        return self.talleres

    def delete(self, *args):
        self.estado_taller = False
        self.save()
        return True
