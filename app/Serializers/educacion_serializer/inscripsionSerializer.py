from rest_framework import serializer
from app.models.educacion_model.inscripsionModel import tarea

class InscRegistroSerializer(serializer.serializer):
     centro_educativo = serializers.CharField(max_length=50)
     alumno = serializers.IntegerField()
     ciclo_grado = serializers.IntegerField()
     Fecha_inscripcion = serializers.DateTimeField()

class InscSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields=(
        'id',
        'centro_educativo',
        'alumno',
        'ciclo_grado',
        'Fecha_inscripcion',
        'estado_incpripsion',
        )
        depth = 2
