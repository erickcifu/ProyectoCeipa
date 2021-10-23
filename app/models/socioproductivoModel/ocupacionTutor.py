from django.db import models

class OcupacionTutor(models.Model):
    ocupacion_tutor = models.CharField(max_length=50)
    estado_ocuptutor = models.BooleanField(default=True)

    def __str__(self):
        return self.ocupacion_tutor

    def delete(self, *args):
        self.estado_ocuptutor = False
        self.save()
        return True
