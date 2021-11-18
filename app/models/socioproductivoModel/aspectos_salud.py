from django.db import models

class AspectosSalud(models.Model):
    fractura = models.BooleanField(default=False)
    descripcion_fractura = models.CharField(max_length=100)
    operacion = models.BooleanField(default=False)
    descripcion_operacion = models.CharField(max_length=50)
    padecimiento = models.BooleanField(default=False)
    descripcion_enfermedad = models.CharField(max_length=100)
    recibe_tratamiento = models.BooleanField(default=False)
    descripcion_tratamiento = models.CharField(max_length=100)
    nombre_medicamento = models.CharField(max_length=50)
    limitacion_fisica = models.BooleanField(default=False)
    descripcion_limitacion = models.CharField(max_length=100)
    estado_aspectosalud = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion_fractura

    def delete(self, *args):
        self.estado_aspectosalud = False
        self.save()
        return True
