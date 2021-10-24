from django.db import models
from .electrodomesticos import Electrodomesticos

class ElectVivienda(models.Model):
    elect = models.ForeignKey(Electrodomesticos, on_delete=models.CASCADE, related_name="electro_viv")
    #vivienda

    def __str__(self):
        return str(self.elect)
