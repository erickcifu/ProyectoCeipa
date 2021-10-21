from django.db import models
from .discapacidad import Discapacidad
from app.models.educacion_model.etnia import etnia
from .gradoAcademico import GradoAcademico
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.genero import genero

class Persona(models.Model):
    persona = models.CharField(max_length=50,null=False)
    apellidos_persona = models.CharField(max_length=100,null=True)
    fecha_nacimiento = models.DateField()
    cui = models.CharField(max_length=13)
    direccion_persona = models.CharField(max_length=80)
    telefono = models.CharField(max_length=8, null=True, blank=True)
    telefonoc = models.CharField(max_length=8, null=True, blank=True)
    fotografia = models.ImageField(upload_to='ceipa', null=True, blank=True)
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="P_muni")
    etni = models.ForeignKey(etnia, on_delete=models.CASCADE, related_name="P_etnia")
    estudios_anteriores = models.ForeignKey(GradoAcademico, on_delete=models.CASCADE, related_name="P_estudios")
    gen = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="P_genero")
    disc = models.BooleanField(default=False)
    estado_persona = models.BooleanField(default=True)

    def __str__(self):
        return self.persona

    def delete(self, *args):
        self.estado_persona = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
