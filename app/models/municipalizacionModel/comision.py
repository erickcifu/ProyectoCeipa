from django.db import models

class Comision(models.Model):
    nombre_comision= models.CharField(max_length=55)
    estado_comision = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_comision

    def delete(self, *args):
        self.estado_comision = False
        self.save()
        return True
