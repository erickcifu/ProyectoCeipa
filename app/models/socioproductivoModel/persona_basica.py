from django.db import models

from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.genero import genero
from .ViviendaSocio import ViviendaSocio
from .info_educacion import InfoEducacion
from .caract_laborales import Caract_laborales
from .aspectos_salud import AspectosSalud
from .info_economica import InfoEconomica
from .encargado import Encargado
from .padres_familia import PadresSociop

class PersonaBasica(models.Model):
    nombresp = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    DPIP = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)
    tel_casa = models.CharField(max_length=8)
    tel_cel = models.CharField(max_length=8)
    email = models.EmailField(max_length=100, null=True, blank=True)
    cantidad_convivientes = models.IntegerField()
    conquien_vive = models.CharField(max_length=100)
    fotografiaP = models.ImageField(upload_to='ceipa', blank=True, null=True)
    municipio = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="PB_municipio")
    etnia = models.ForeignKey(etnia, on_delete=models.CASCADE, related_name="PB_etnia")
    genero = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="PB_genero")
    vivienda_socio = models.ForeignKey(ViviendaSocio, on_delete=models.CASCADE, related_name="PB_viviendasocio")
    info_educacion = models.ForeignKey(InfoEducacion, on_delete=models.CASCADE, related_name="PB_info_educacion")
    c_laborales = models.ForeignKey(Caract_laborales, on_delete=models.CASCADE, related_name="PB_CaracteristicasLaborales")
    aspectos_salud = models.ForeignKey(AspectosSalud, on_delete=models.CASCADE, related_name="PB_aspectos_salud")
    razon = models.CharField(max_length=200)
    info_economica = models.ForeignKey(InfoEconomica, on_delete=models.CASCADE, related_name="PB_info_economica")
    ingreso_total = models.FloatField()
    total_gastos = models.FloatField(null=True, blank=True)
    edad = models.IntegerField(null=True, default=None, blank=True)
    tutor_socio = models.ForeignKey(Encargado, on_delete=models.CASCADE, related_name="PB_tutor_socio")
    padres = models.ForeignKey(PadresSociop, on_delete=models.CASCADE, related_name="PB_padres")
    estado_persona_basica = models.BooleanField(default="True")

    @property
    def foto_url(self):
        if self.fotografia and hasattr(self.fotografia, 'url'):
            return self.fotografia.url


    def __str__(self):
        return self.persona_basica

    def delete(self, *args):
        self.estado_persona_basica = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
