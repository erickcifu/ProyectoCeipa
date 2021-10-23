from django.db import models

class GrupoNA(models.Model):
    nombre_grupona = models.CharField(max_length=150)
    estado_grupona = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_grupo

    def delete(self, *args):
        self.estado_grupona = False
        self.save()
        return True
