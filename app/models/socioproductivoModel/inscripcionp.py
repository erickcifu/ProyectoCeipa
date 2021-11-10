from django.db import models
from .persona_basica import PersonaBasica
from .talleres import Taller
from app.models.educacion_model.municipioModel import municipio

class Inscripcionp(models.Model):
    insc_persona = models.ForeignKey(PersonaBasica, on_delete=models.CASCADE, related_name="ins_per")
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, related_name='asig_talleres')
    lugar_inscripcion = models.ForeignKey(municipio, on_delete=models.CASCADE, related_name='muni_insc')
    inicio_taller = models.DateField()
    final_taller = models.DateField()
    certificado_taller = models.BooleanField(default=False)

    def __str__(self):
        return str(self.insc_persona)
