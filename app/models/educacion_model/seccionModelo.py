from django.db import models

class seccion(models.Model):
    nombre_seccion = models.CharField(max_length=255,null=False )
    estado_seccion = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_seccion

    def delete(self, *args):
        self.estado_seccion = False
        self.save()
        return True
