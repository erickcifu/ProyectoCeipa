from django.db import models

class Caract_laborales(models.Model):
    ha_trabajado = models.BooleanField(default=False)
    razon_t = models.CharField(max_length=255, null=True, blank=True)
    edad_inicio = models.CharField(max_length=50, null=True, blank=True)
    t_realizados = models.CharField(max_length=100, null=True, blank=True)
    trabaja_actualmente = models.BooleanField(default=False)
    empleador_p = models.CharField(max_length=100, null=True, blank=True)
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    fam_extranjero = models.BooleanField(default=False)
    op_extranjero = models.BooleanField(default=False)
    op_empleos = models.BooleanField(default=False)
    empleado = models.BooleanField(default=False)
    propio = models.BooleanField(default=False)
    s_americano = models.BooleanField(default=False)
    estado_claborales = models.BooleanField(default=True)

    def __str__(self):
        return self.empleador_p

    def delete(self, *args):
        self.estado_claborales = False
        self.save()
        return True
