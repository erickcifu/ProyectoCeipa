from django.db import models

class Electrodomesticos(models.Model):
    Nombre_electro = models.CharField(max_length=30)
    estado_electro = models.BooleanField(default=True)

    def __str__(self):
        return self.servicio

    def delete(self, *args):
        self.estado_electro = False
        self.save()
        return True
