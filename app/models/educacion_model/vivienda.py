from django.db import models

class vivienda(models.Model):
    cantidad_personas = models.IntegerField()
    cantidad_ambientes = models.IntegerField()
    energia_electrica = models.BooleanField(default=False)
    servicio_sanitario = models.BooleanField(default=False)
    letrina = models.BooleanField(default=False)
    #Foreignkey tipo de techo
    #Foreignkey categoria
    #Foreignkey tipo de piso
    #Foreignkey sericio de agua
    #Foreignkey alumno
    estado_vivienda = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_vivienda = False
        self.save()
        return True
