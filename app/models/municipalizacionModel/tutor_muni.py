from django.db import models

class Tutor(models.Model):
    nombres_tutor = models.CharField(max_length=50,null=False)
    apellidos_tutor = models.CharField(max_length=50,null=True)
    DPI = models.IntegerField()
    estado_tutor = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()
    direccion_tutor = models.CharField(max_length=80)
    telefono = models.CharField(max_length=8)
    fotografia = models.ImageField(upload_to='ceipa', null=True, blank=True)


    def delete(self, *args):
        self.estado_tutor = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True

    def __str__(self):
        return '{}'.format(self.nombres_tutor)
