from rest_framework import serializers
from app.models import Ciclo_grado

class cgRegistroSerializer(serializers.Serializer):
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
