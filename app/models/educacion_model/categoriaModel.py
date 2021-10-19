from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=55,null=False)
    descripcion_categoria = models.CharField(max_length=100,null=True, blank=True)
    estado_categoria = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_categoria

    def delete(self, *args):
        self.estado_categoria = False
        self.save()
        return True
