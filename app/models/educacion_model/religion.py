from django.db import models

class religion(models.Model):
    nombre_religion = models.CharField(max_length=50,null=False )
    estado_religion = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_religion

    def delete(self, *args):
        self.estado_religion = False
        self.save()
        return True
