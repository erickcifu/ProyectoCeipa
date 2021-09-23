from rest_framework import serializers
from app.models import Ciclo

class cicloRegistroSerializer(serializers.Serializer):
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
