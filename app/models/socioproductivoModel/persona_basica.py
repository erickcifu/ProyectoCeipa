from django.db import models

from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.genero import genero
from .info_educacion import InfoEducacion
from .caract_laborales import Caract_laborales
from .aspectos_salud import AspectosSalud
from .encargado import Encargado
from .padres_familia import PadresSociop
from .ViviendaSocio import ViviendaSocio

class PersonaBasica(models.Model):
    nombresp = models.CharField(max_length=100)
    apellidosp = models.CharField(max_length=100)
    fecha_nacimientop = models.DateField()
    DPIP = models.CharField(max_length=13)
    direccionp = models.CharField(max_length=100, null=True, blank=True)
    tel_casap = models.CharField(max_length=8, null=True, blank=True)
    tel_celp = models.CharField(max_length=8, null=True, blank=True)
    emailp = models.EmailField(max_length=100, null=True, blank=True)
    cantidad_convivientesp = models.IntegerField()
    conquien_vive = models.CharField(max_length=100)
    fotografiaP = models.ImageField(upload_to='ceipa', blank=True, null=True)
    municipio = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="PB_municipio")
    etnia = models.ForeignKey(etnia, on_delete=models.CASCADE, related_name="PB_etnia")
    genero = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="PB_genero")
    vivienda_socio = models.ForeignKey(ViviendaSocio, on_delete=models.CASCADE, related_name="PB_1viviendasocio")
    info_educacion = models.ForeignKey(InfoEducacion, on_delete=models.CASCADE, related_name="PB_info_educacion", null=True, blank=True)
    caract_laborales = models.ForeignKey(Caract_laborales, on_delete=models.CASCADE, related_name="PB_Carac_laborales", null=True, blank=True)
    aspectos_salud = models.ForeignKey(AspectosSalud, on_delete=models.CASCADE, related_name="PB_aspectos_salud", null=True, blank=True)
    razon = models.CharField(max_length=200, null=True, blank=True)
    ingreso_total = models.FloatField()
    total_gastos = models.FloatField(null=True, blank=True)
    edad = models.IntegerField(null=True, default=None, blank=True)
    tutor_socio = models.ForeignKey(Encargado, on_delete=models.CASCADE, related_name="PB_tutor_socio", null=True, blank=True)
    padres = models.ForeignKey(PadresSociop, on_delete=models.CASCADE, related_name="PB_padres", null=True, blank=True)
    estado_persona_basica = models.BooleanField(default=True)

    @property
    def foto_url(self):
        if self.fotografiaP and hasattr(self.fotografiaP, 'url'):
            return self.fotografiaP.url


    def __str__(self):
        return self.nombresp

    def delete(self, *args):
        self.estado_persona_basica = False
        if self.fotografiaP is not  None:
            self.fotografiaP.delete()
        self.save()
        return True
