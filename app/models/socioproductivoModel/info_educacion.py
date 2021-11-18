from django.db import models
from .jornada_estudio import JornadaEstudios
from .grado_actual import Grado_actual
from .grupo_na import GrupoNA

class InfoEducacion(models.Model):
    nombre_establecimiento = models.CharField(max_length=30)
    direccion_establecimiento = models.CharField(max_length=50)
    jornada_estudio = models.ForeignKey(JornadaEstudios, on_delete=models.CASCADE, related_name="I_jornada")
    grado_actual = models.ForeignKey(Grado_actual, on_delete=models.CASCADE, related_name="I_gradoactual")
    nombre_maestro = models.CharField(max_length=50, null=True, blank=True)
    tel_maestro = models.CharField(max_length=8, null=True, blank=True)
    participacion_grupo = models.BooleanField(default=False)
    grupo_nin_adole = models.ForeignKey(GrupoNA, on_delete=models.CASCADE, related_name="I_Grupo", null=True, blank=True)
    recibido_formacion = models.BooleanField(default=False)
    conocimiento_derechoshumanos = models.CharField(max_length=100)
    conocimiento_leyes = models.BooleanField(default=False)
    importancia_organizacion = models.BooleanField(default=False)
    te_motiva_participar = models.BooleanField(default=False)
    estado_info_educacion = models.BooleanField(default=100)

    def __str__(self):
        return self.nombre_establecimiento

    def delete(self, *args):
        self.estado_info_educacion = False
        self.save()
        return True
