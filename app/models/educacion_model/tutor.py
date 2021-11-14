from django.db import models
from .municipioModel import municipio
from .genero import genero
from .parentesco import Parentesco

class Tutor(models.Model):
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="Mu_muni")
    genero = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="Ge_genero")
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE, related_name="Pa_parentesco")
    nombres_tutor = models.CharField(max_length=50)
    apellidos_tutor = models.CharField(max_length=50)
    DPI_tutor = models.CharField(max_length=13)
    estado_tutor = models.BooleanField(default=True)
    fecha_nacimiento_tutor = models.DateField()
    direccion_tutor = models.CharField(max_length=80, null=True, blank=True)
    telefono_tutor = models.CharField(max_length=8, blank=True, null=True)
    fotografia_t = models.ImageField(upload_to='ceipa', null=True, blank=True)
    correo_tutor = models.EmailField(max_length=80, null=True, blank=True)
    ocupacion_tutor = models.CharField(max_length=100, null=True,blank=True)

    @property
    def foto_url(self):
        if self.fotografia_t and hasattr(self.fotografia_t, 'url'):
            return self.fotografia_t.url

    def __str__(self):
        return self.nombres_tutor

    def delete(self, *args):
        self.estado_tutor = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
