from django.db import models

class GradoAcademico(models.Model):
    nombre_academico = models.CharField(max_length=50)
    descripcion_academico = models.CharField(max_length=255, null=True, blank=True)
    estado_academico = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_academico

    def delete(self, *args):
        self.estado_academico = False
        self.save()
        return True
