from django.db import models
from app.models.educacion_model.centro_educativo import centro_educativo
from app.models.educacion_model.personalEducativo import personalEducativo

class Centropersona(models.Model):
    centro_Educativo =models.ForeignKey(centro_educativo, on_delete=models.CASCADE, related_name="c_educativo")
    personal =models.ForeignKey(personalEducativo, on_delete=models.CASCADE, related_name="p_educativo")
    estado_centropersona = models.BooleanField(default=True)

    def __str__(self):
        return self.centro_Educativo

    def delete(self, *args):
        self.estado_centropersona = False
        self.save()
        return True
