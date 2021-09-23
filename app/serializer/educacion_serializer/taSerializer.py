from rest_framework import serializers
from app.models import tarea_alumno

class TARegistroSerializer(serializers.Serializer):
    tarea = serializers.IntegerField()
    alumno = serializers.IntegerField()
    nota_obtenida = serializers.FloatField()

class TASerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea_alumno
        fields=(
            'id',
            'tarea',
            'alumno',
            'nota_obtenida',
            'observaciones',
            'estado_entrega',
            'estado_tareaAlumno',
        )
        depth = 2
