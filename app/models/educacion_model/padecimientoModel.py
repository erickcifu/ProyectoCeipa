from django.db import models


class Padecimiento(models.Model):
    nombre_padecimiento = models.CharField(max_length=205,null=False )
    estado_padecimiento = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_padecimiento

    def delete(self, *args):
        self.estado_padecimiento = False
        self.save()
        return True
