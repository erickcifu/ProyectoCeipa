from django.db import models

class Cargo(models.Model):
    nombre_cargo= models.CharField(max_length=55)
    estado_cargo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_cargo

    def delete(self, *args):
        self.estado_cargo = False
        self.save()
        return True
