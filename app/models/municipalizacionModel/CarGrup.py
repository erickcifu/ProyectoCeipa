from django.db import models

class CargoGrupo(models.Model):
    nombre_cg= models.CharField(max_length=55)
    estado_cg = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_cg

    def delete(self, *args):
        self.estado_cg = False
        self.save()
        return True
