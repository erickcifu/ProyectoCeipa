from django.db import models
from .tipo_techo import Tipo_techo
from .categoriaModel import Categoria
from .tipopisoModel import Tipo_piso
from .servicio_agua import Servicio_Agua
from .tipo_muro import Tipo_muro
from .alumnoModelo  import Alumno

class vivienda(models.Model):
    cantidad_personas = models.IntegerField()
    cantidad_ambientes = models.IntegerField()
    energia_electrica = models.BooleanField(default=False)
    servicio_sanitario = models.BooleanField(default=False)
    letrina = models.BooleanField(default=False)
    techo = models.ForeignKey(Tipo_techo, on_delete=models.CASCADE, related_name="techo_vivienda")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="cat_vivienda")
    piso = models.ForeignKey(Tipo_piso, on_delete=models.CASCADE, related_name="piso_vivienda")
    muro = models.ForeignKey(Tipo_muro, on_delete=models.CASCADE, related_name="T_muro")
    servicio = models.ForeignKey(Servicio_Agua, on_delete=models.CASCADE, related_name="servicio_vivienda")
    estudiante = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="estudiante_vivieda")
    servicio_internet = models.BooleanField(default=False)
    estado_vivienda = models.BooleanField(default=True)

    def __str__(self):
        return str(self.estudiante)

    def delete(self, *args):
        self.estado_vivienda = False
        self.save()
        return True
