from django.db import models

class GOrganizado(models.Model):
    nombre_grupo = models.CharField(max_length=255,null=False)
    estado_grupo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_grupo

    def delete(self, *args):
        self.estado_grupo = False
        self.save()
        return True
