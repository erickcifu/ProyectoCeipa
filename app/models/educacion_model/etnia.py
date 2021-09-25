from django.db import models

class etnia(models.Model):
    nombre_etnia = models.CharField(max_length=50,null=False )
    descripcion_etnia = models.CharField(max_length=100,null=True, blank=True)
    estado_etnia = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_etnia

    def delete(self, *args):
        self.estado_etnia = False
        self.save()
        return True
