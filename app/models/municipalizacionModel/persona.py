from django.db import models
from .discapacidad import Discapacidad
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.estudiosantModel import EstudiosAnt
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.genero import genero

class Persona(models.Model):
    persona = models.CharField(max_length=50,null=False)
    apellidos_persona = models.CharField(max_length=100,null=True)
    fecha_nacimiento = models.DateField()
    cui = models.IntegerField()
    direccion_persona = models.CharField(max_length=80)
    telefono = models.CharField(max_length=8)
    telefonoc = models.CharField(max_length=8)
    fotografia = models.ImageField(upload_to='ceipa', null=True, blank=True)
    estado_persona = models.BooleanField(default=True)

    muni = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="P_muni")
    etni = models.ForeignKey(etnia, on_delete=models.CASCADE, related_name="P_etnia")
    estudios_anteriores = models.ForeignKey(EstudiosAnt, on_delete=models.CASCADE, related_name="P_estudios")
    gen = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="P_genero")
    disc = models.ForeignKey(Discapacidad, on_delete=models.CASCADE, related_name="T_disc")

    def __str__(self):
        return self.nombres_persona

    def delete(self, *args):
        self.estado_persona = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
