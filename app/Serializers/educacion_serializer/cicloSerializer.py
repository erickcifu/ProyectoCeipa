from rest_framework import serializer
from app.models.educacion_model.ciclo import Ciclo

class cicloRegistroSerializer(serializer.serializer):
    anio = serializers.IntegerField()

class cicloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo
        fields=(
        'id',
        'anio',
        'estado_ciclo',
        )
        depth = 2
