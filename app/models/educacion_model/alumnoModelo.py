from django.db import models
from .ocupacion import ocupacion
from .tutor import Tutor
from .etnia import etnia
from .idioma import idioma
from .estudiosantModel import EstudiosAnt
from .municipioModel import municipio
from .genero import genero


class Alumno(models.Model):
    ocup = models.ForeignKey(ocupacion, on_delete=models.CASCADE, related_name="O_ocupacion")
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name="T_tutor")
    etni = models.ForeignKey(etnia, on_delete=models.CASCADE, related_name="E_etnia")
    idiome = models.ForeignKey(idioma, on_delete=models.CASCADE, related_name="I_idioma")
    estudios_anteriores = models.ForeignKey(EstudiosAnt, on_delete=models.CASCADE, related_name="EA_estudios")
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name="M_muni")
    gen = models.ForeignKey(genero, on_delete=models.CASCADE, related_name="G_genero")
    nombres_alumno = models.CharField(max_length=50,null=False)
    cui = models.IntegerField()
    apellidos_alumno = models.CharField(max_length=100,null=True)
    codigo_mineduc = models.IntegerField()
    estado_alumno = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()
    ingreso_familiar = models.FloatField(null=True, blank=True)
    direccion_alumno = models.CharField(max_length=80, null=True, blank=True)
    telefono = models.CharField(max_length=8, null=True, blank=True)
    fotografia = models.ImageField(upload_to='ceipa', blank=True, null=True)

    @property
    def foto_url(self):
        if self.fotografia and hasattr(self.fotografia, 'url'):
            return self.fotografia.url
        

    def __str__(self):
        return self.nombres_alumno

    def delete(self, *args):
        self.estado_alumno = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
