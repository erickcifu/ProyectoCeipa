from django.db import models
from .electrodomesticos import Electrodomesticos
from .ViviendaSocio import ViviendaSocio

class ElectVivienda(models.Model):
    elect = models.ForeignKey(Electrodomesticos, on_delete=models.CASCADE, related_name="electro_viv")
    vivienda = models.ForeignKey(ViviendaSocio, on_delete=models.CASCADE, related_name="electrodomest_viv")

    def __str__(self):
        return str(self.elect)
