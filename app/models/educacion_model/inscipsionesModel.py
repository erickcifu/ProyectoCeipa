from django.db import models
from app.models.educacion_model.centro_educativo import centro_educativo
from app.models.educacion_model.alumnoModelo import Alumno
from app.models.educacion_model.ciclo_grado import Ciclo_grado
from app.models.educacion_model.centro_educativo import centro_educativo


class Inscripcion(models.Model):
    centro_educativo = models.ForeignKey(centro_educativo, on_delete=models.CASCADE, related_name="C_educativo")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="A_alumnos")
    ciclo_grado = models.ForeignKey(Ciclo_grado, on_delete=models.CASCADE, related_name="ciclo_grado")
    Fecha_inscripcion = models.DateTimeField()
    alumno_promovido = models.BooleanField(default=False)
    alumno_retirado = models.BooleanField(default=False)
    alumno_promovido = models.BooleanField(default=False)
    alumno_retirado = models.BooleanField(default=False)
    estado_incpripsion = models.BooleanField(default=True)

    def __str__(self):
        return self.centro_educativo

    def delete(self, *args):
        self.estado_incpripsion = False
        self.save()
        return True
