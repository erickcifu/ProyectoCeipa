from django.db import models

class idioma(models.Model):
    nombre_idioma = models.CharField(max_length=50, null=False)
    descripcion_idioma = models.CharField(max_length=255, null=True, blank=True)
    estado_idioma = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_idioma

    def delete(self, *args):
        self.estado_idioma = False
        self.save()
        return True
