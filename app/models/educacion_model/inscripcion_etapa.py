from django.db import models
from app.models.educacion_model.centro_educativo import centro_educativo
from app.models.educacion_model.alumnoModelo import Alumno
from .ciclo_etapa import Ciclo_etapa
from .etapa import Etapa

class Inscripcion_etapa(models.Model):
    centro_educ_etapa = models.ForeignKey(centro_educativo, on_delete=models.CASCADE, related_name="centro_etapa")
    alumno_etapa = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="insc_alumn_etapa")
    ciclo_etapa = models.ForeignKey(Ciclo_etapa, on_delete=models.CASCADE, related_name="ce_insc")
    etapa_promovido = models.BooleanField(default=False)
    etapa_retirado = models.BooleanField(default=False)
    insc_etapa_estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.alumno_etapa)

    def delete(self, *args):
        self.insc_etapa_estado = False
        self.save()
        return True
