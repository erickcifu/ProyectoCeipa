from django.db import models

class Institucion(models.Model):
    nombre_ins = models.CharField(max_length=255,null=False)
    correo = models.EmailField(max_length=55, null=True, blank=True)
    estado_ins = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_ins
        
    def delete(self, *args):
        self.estado_ins = False
        self.save()
        return True
