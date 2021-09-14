from django.db import models

class Alumno(models.Model):
    nombres_alumno = models.CharField(max_length=50,null=False )
    cui = models.IntegerField(max_length=13,null=False)
    apellidos_alumno = models.CharField(max_length=100,null=True)
    codigo_mineduc = models.IntegerField(max_length=20,null=False)
    estado_alumno = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()
    ingreso_familiar = models.FloatField()
    direccion_alumno = models.CharField(max_length=80)
    GENEROS = (
        (0, 'Masculino'),
        (1, 'Femenino'),
        (2, 'Otro')
    )
    genero = models.CharField(choices=GENEROS, max_length=2)
    telefono = models.CharField(max_length=8)
    fotografia = models.ImageField()


    def delete(self, *args):
        self.estado_alumno = False
        self.save()
        return True
