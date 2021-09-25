from django.db import models

class Ausencia(models.Model):
    iniciof = models.DateTimeField()
    finf = models.DateTimeField()
    razon = models.CharField(max_length=255,null=False)
    estado_ausencia = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_ausencia = False
        self.save()
        return True
