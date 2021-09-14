from django.db import models

class Servicio_Agua(models.Model):
    servicio_agua = models.CharField(max_length=50, null=False)
    descripcion_servicio_agua = models.CharField(max_length=100,null=True, blank=True)
    estado_agua = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_agua = False
        self.save()
        return True