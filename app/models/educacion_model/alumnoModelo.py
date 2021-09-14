from django.db import models

class etnia(models.Model):
    nombre_etnia = models.CharField(max_length=50,null=False )
    descripcion_etnia = models.CharField(max_length=100,null=True, blank=True)
    estado_etnia = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_ocupacion = False
        self.save()
        return True
