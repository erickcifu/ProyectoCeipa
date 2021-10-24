from django.db import models
from .jornada_estudio import JornadaEstudios
#from .grado_actual import GradoActual
#from .grupo_nin_adol import GrupoNinAdol

class InfoEducacion(models.Model):
    nombre_establecimiento = models.CharField(max_length=30)
    direccion_establecimiento = models.CharField(max_length=50)
    jornada_estudio = models.ForeignKey(JornadaEstudios, on_delete=models.CASCADE, related_name="I_jornada")
    #grado_actual = models.ForeignKey(GradoActual, on_delete=models.CASCADE, related_name="I_gradoactual")
    nombre_maestro = models.CharField(max_length=50)
    tel_maestro = models.CharField(max_length=8)
    #grupo_nin_adole = models.ForeignKey(GrupoNinAdol, on_delete=models.CASCADE, related_name="I_Grupo")
    nombre_grupo = models.CharField(max_length=30)
    descripcion_grupo = models.CharField(max_length=50)
    recibido_formacion = models.CharField(max_length=100)
    conocimiento_derechoshumanos = models.CharField(max_length=100)
    conocimiento_leyes = models.BooleanField(default=True)
    importancia_organizacion = models.CharField(max_length=100)
    te_motiva_participar = models.CharField(max_length=100)
    que_esperas_participar = models.CharField(max_length=100)
    estado_info_educacion = models.BooleanField(default=100)

    def __str__(self):
        return self.info_educacion

    def delete(self, *args):
        self.estado_info_educacion = False
        self.save()
        return True