from django.db import models

class JornadaEstudios(models.Model):
    jornada = models.CharField(max_length=50)
    estado_joranadaes = models.BooleanField(default=True)

    def __str__(self):
        return self.jornada

    def delete(self, *args):
        self.estado_joranadaes = False
        self.save()
        return True
