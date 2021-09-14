from django.db import models
from app.models.educacion_model import Parentesco

class Conviviente(models.Model):
    nombres_conviviente = models.CharField(max_length=50,null=False )
    apellidos_conviviente = models.CharField(max_length=100,null=True)
    estado_conviviente = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField()
    
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE)


    def delete(self, *args):
        self.estado_conviviente = False
        self.save()
        return True