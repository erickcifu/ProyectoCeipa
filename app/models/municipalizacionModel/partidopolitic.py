from django.db import models

class PartidoPolitic(models.Model):
    nombre_partido = models.CharField(max_length=50,null=False)
    estado = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado = False
        self.save()
        return True

    def __str__(self):
        return '{}'.format(self.nombre_partido)