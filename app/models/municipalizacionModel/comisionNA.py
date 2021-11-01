from django.db import models
from .persona import Persona
from .CarGrup import CargoGrupo
from .Gorganizado import GOrganizado

class ComisionNA(models.Model):
    persona_cna = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="comision_pers")
    correo_personacna = models.EmailField(max_length=100, null=True, blank=True)
    participacion_comina = models.BooleanField(default=False)
    gorg_comision = models.ForeignKey(GOrganizado, on_delete=models.CASCADE, related_name="gorga_comina")
    cg_comision = models.ForeignKey(CargoGrupo, on_delete=models.CASCADE, related_name="carg_comina")
    inst_gobierno = models.BooleanField(default=False)
    inst_publica = models.BooleanField(default=False)
    nombre_instit = models.CharField(max_length=255,null=False)
    correo_instit = models.EmailField(max_length=55, null=True, blank=True)
    tel_instit = models.CharField(max_length=8, null=True, blank=True)
    vacuna_comision = models.BooleanField(default=True)
    estado_comision = models.BooleanField(default=True)

    def __str__(self):
        return str(self.persona_cna)

    def delete(self, *args):
        self.estado_comision = False
        self.save()
        return True
