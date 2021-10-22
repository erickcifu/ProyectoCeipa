from django.db import models

class TipoEmp(models.Model):
    emprendimiento_tipo = models.CharField(max_length=100)
    estado_tipoEmp = models.BooleanField(default=True)

    def __str__(self):
        return self.emprendimiento_tipo

    def delete(self, *args):
        self.estado_tipoEmp = False
        self.save()
        return True
