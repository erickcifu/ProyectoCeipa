from django.db import models
from app.models.educacion_model.ocupacion import ocupacion
#from app.models.educacion_model.tutor import tutor
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.idioma import idioma
#from app.models.educacion_model.estudios import
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.genero import genero


class Alumno(models.Model):
    ocup = models.ForeignKey(ocupacion, on_delete=models.CASCADE)
    #tutor = models.ForeignKey()
    etni = models.ForeignKey(etnia, on_delete=models.CASCADE)
    idiome = models.ForeignKey(idioma, on_delete=models.CASCADE)
    #estuds = models.ForeignKey() 
    muni = models.ForeignKey(municipio, on_delete=models.CASCADE)
    gen = models.ForeignKey(genero, on_delete=models.CASCADE)

    nombres_alumno = models.CharField(max_length=50,null=False )
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
