from django.db import models

class departamento(models.Model):
    nombre_departamento = models.CharField(max_length=50, null=False)
    estado_departamento = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_departamento = False
        self.save()
        return True
