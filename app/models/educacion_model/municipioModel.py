from django.db import models
from app.models.educacion_model.departamento import departamento

class municipio(models.Model):
    dep =models.ForeignKey(departamento, on_delete=models.CASCADE, related_name="M_dep")
    nombre_municipio = models.CharField(max_length=255,null=False )
    estado_municipio = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_municipio

    def delete(self, *args):
        self.estado_municipio = False
        self.save()
        return True
