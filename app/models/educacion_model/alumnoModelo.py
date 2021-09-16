from django.db import models
from .ocupacion import ocupacion
#from .tutor import tutor
from .etnia import etnia
from .idioma import idioma
#from .estudios import
from .municipioModel import municipio
from .genero import genero
from .religion_alumno import Religion_alumno

class Alumno(models.Model):
    ocup = models.ForeignKey(ocupacion, on_delete=models.CASCADE)
    #tutor = models.ForeignKey()
    etni = models.ForeignKey(etnia, on_delete=models.CASCADE)
    idiome = models.ForeignKey(idioma, on_delete=models.CASCADE)
    #estuds = models.ForeignKey()
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE)
    gen = models.ForeignKey(genero, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion_alumno, on_delete=models.CASCADE)

    nombres_alumno = models.CharField(max_length=50,null=False)
    cui = models.IntegerField(max_length=13,null=False)
    apellidos_alumno = models.CharField(max_length=100,null=True)
    codigo_mineduc = models.IntegerField(max_length=20,null=False)
    estado_alumno = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()
    ingreso_familiar = models.FloatField()
    direccion_alumno = models.CharField(max_length=80)
    telefono = models.CharField(max_length=8)
    fotografia = models.ImageField()


    def delete(self, *args):
        self.estado_alumno = False
        self.save()
        return True
