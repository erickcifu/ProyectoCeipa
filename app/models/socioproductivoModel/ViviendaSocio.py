from django.db import models

from app.models.educacion_model.tipopisoModel import Tipo_piso
from app.models.educacion_model.tipo_techo import Tipo_techo
from app.models.educacion_model.tipo_muro import Tipo_muro
from app.models.educacion_model.categoriaModel import Categoria


class ViviendaSocio(models.Model):
    numero_habitantes = models.IntegerField()
    otra_Viv = models.BooleanField(default=False)
    desc_Otra_Viv = models.CharField(max_length=100, null=True, blank=True)
    Telefono = models.BooleanField(default=False)
    tipopiso = models.ForeignKey(Tipo_piso, on_delete=models.CASCADE, related_name="VS_Tipo_piso")
    tipotecho = models.ForeignKey(Tipo_techo, on_delete=models.CASCADE, related_name="Tipo_techo")
    tipomuro = models.ForeignKey(Tipo_muro, on_delete=models.CASCADE, related_name="VS_Tipo_muro")
    tipovivienda = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="VS_Categoria")
    agua_potable = models.BooleanField(default=False)
    energia_elect = models.BooleanField(default=False)
    dreaje = models.BooleanField(default=False)
    servicio_telefono = models.BooleanField(default=False)
    nivel_Eco_Alto = models.BooleanField(default=False)
    nivel_Eco_medio = models.BooleanField(default=False)
    nivel_Eco_bajo = models.BooleanField(default=False)
    pobre = models.BooleanField(default=False)
    no_pobre = models.BooleanField(default=False)
    Extemadamente_pobre = models.BooleanField(default=False)
    estado_vivsocio = models.BooleanField(default=True)


    def __str__(self):
        return str(self.numero_habitantes)

    def delete(self, *args):
        self.estado_vivsocio = False
        self.save()
        return True
