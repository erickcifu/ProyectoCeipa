from django.db import models
from .municipioModel import municipio
from .genero import genero
from .parentesco import Parentesco

class Tutor(models.Model):
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="Mu_muni")
    genero = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="Ge_genero")
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE, related_name="Pa_parentesco")
    nombres_tutor = models.CharField(max_length=50,null=False)
    apellidos_tutor = models.CharField(max_length=50,null=True)
    DPI = models.IntegerField()
    estado_tutor = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()
    direccion_tutor = models.CharField(max_length=80)
    telefono = models.CharField(max_length=8)
    fotografia = models.ImageField(upload_to='ceipa', null=True, blank=True)
    correo = models.EmailField(max_length=80)


    def delete(self, *args):
        self.estado_tutor = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
