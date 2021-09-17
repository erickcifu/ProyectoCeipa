from django.db import models


class Padecimiento(models.Model):
    nombre_padecimiento = models.CharField(max_length=205,null=False )
    estado_padecimiento = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_psicologico = False
        self.save()
        return True
