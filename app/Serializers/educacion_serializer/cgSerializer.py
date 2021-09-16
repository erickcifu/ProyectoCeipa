from rest_framework import serializer
from app.models.educacion_model.ciclo_grado import Ciclo_grado

class cgRegistroSerializer(serializer.serializer):
    grado = serializers.IntegerField()
    ciclo = serializers.IntegerField()
    seccion = serializers.IntegerField()

class cgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo_grado
        fields=(
        'id',
        'grado',
        'ciclo',
        'seccion',
        'estado_cg',
        )
        depth = 2
