from django.db import models

class grados(models.Model):
    nombre_grados = models.CharField(max_length=50,null=False )
    descripcion_grados = models.CharField(max_length=255, null=True, blank=True)
    estado_grados = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_grados = False
        self.save()
        return True
