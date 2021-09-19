from django.db import models
from .religion import religion
from app.models.educacion_model.alumnoModelo import Alumno

class Religion_alumno(models.Model):
    religion = models.ForeignKey(religion, on_delete=models.CASCADE, related_name="r_religion")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="R_alumno")
    nombre_iglesia = models.CharField(max_length=50,null=False)
    estado_religionalumno = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_religionalumno = False
        self.save()
        return True
