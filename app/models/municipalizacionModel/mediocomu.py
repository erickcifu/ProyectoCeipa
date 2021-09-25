from django.db import models
#from .persona import Persona
#from .cargo import Cargo

class MedioComuni(models.Model):
    #persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="P_persona")
    #cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="C_cargo")
    nombre_medio = models.CharField(max_length=50,null=False)
    correo = models.EmailField(max_length=55, null=True, blank=True)
    telefono = models.CharField(max_length=8)
    estado = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado = False
        self.save()
        return True