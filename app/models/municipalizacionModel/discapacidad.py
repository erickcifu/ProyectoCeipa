from django.db import models

class Discapacidad(models.Model):
    nombre_dis= models.CharField(max_length=55,null=False)
    estado_dis = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_dis

    def delete(self, *args):
        self.estado_dis = False
        self.save()
        return True
