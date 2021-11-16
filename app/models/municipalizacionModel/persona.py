from django.db import models
from app.models.educacion_model.etnia import etnia
from .gradoAcademico import GradoAcademico
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.genero import genero

class Persona(models.Model):
    persona = models.CharField(max_length=50,null=False)
    apellidos_persona = models.CharField(max_length=100,null=True)
    cui_persona = models.CharField(max_length=13)
    direccion_persona = models.CharField(max_length=80)
    telefono_Persona = models.CharField(max_length=8, null=True, blank=True)
    telefonoc_per = models.CharField(max_length=8, null=True, blank=True)
    fotografia_persona = models.ImageField(upload_to='ceipa', null=True, blank=True)
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="P_muni")
    etni = models.ForeignKey(etnia, on_delete=models.CASCADE, related_name="P_etnia")
    estudios_anteriores = models.ForeignKey(GradoAcademico, on_delete=models.CASCADE, related_name="P_estudios")
    gen = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="P_genero")
    disc = models.BooleanField(default=False)
    estado_persona = models.BooleanField(default=True)

    @property
    def foto_url(self):
        if self.fotografia_persona and hasattr(self.fotografia_persona, 'url'):
            return self.fotografia_persona.url

    def __str__(self):
        return self.persona

    def delete(self, *args):
        self.estado_persona = False
        if self.fotografia_persona is not  None:
            self.fotografia_persona.delete()
        self.save()
        return True
