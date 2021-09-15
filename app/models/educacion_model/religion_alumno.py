from django.db import models
from .religion import religion

class Religion_alumno(models.Model):
    relig = models.ForeignKey(religion, on_delete=models.CASCADE)
    nombre_iglesia = models.CharField(max_length=50,null=False )
    estado_religionalumno = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_religionalumno = False
        self.save()
        return True
