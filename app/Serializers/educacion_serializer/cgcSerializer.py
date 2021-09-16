from rest_framework import serializer
from app.models.educacion_model.ciclo_grado_curso import Ciclo_grado_curso

class cgcRegistroSerializer(serializer.serializer):
    maestro = serializers.IntegerField()
    curso = serializers.IntegerField()
    ciclo_grado = serializers.IntegerField()

class cgcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo_grado_curso
        fields=(
        'id',
        'maestro',
        'curso',
        'ciclo_grado',
        'estado_cgc',
        )
        depth = 2
