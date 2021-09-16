from django.db import models
from .tipo_techo import Tipo_techo
from .categoriaModel import categoria
from .tipopisoModel import Tipo_piso
from .servicio_agua import Servicio_Agua
from .alumnoModelo  import Alumno

class vivienda(models.Model):
    cantidad_personas = models.IntegerField()
    cantidad_ambientes = models.IntegerField()
    energia_electrica = models.BooleanField(default=False)
    servicio_sanitario = models.BooleanField(default=False)
    letrina = models.BooleanField(default=False)
    techo = models.Foreignkey(Tipo_techo, on_delete=model.CASCADE, related_name="techo_vivienda")
    categoria = models.Foreignkey(categoria, on_delete=model.CASCADE, related_name="cat_vivienda")
    piso = models.Foreignkey(Tipo_piso, on_delete=models.CASCADE, related_name="piso_vivienda")
    servicio = models.Foreignkey(Servicio_Agua, on_delete=models.CASCADE, related_name="servicio_vivienda")
    estudiante = models.Foreignkey(Alumno, on_delete=models.CASCADE, related_name="estudiante_vivieda")
    estado_vivienda = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_vivienda = False
        self.save()
        return True
