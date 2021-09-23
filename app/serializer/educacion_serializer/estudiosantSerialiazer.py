from rest_framework import serializers
from app.models import EstudiosAnt

class estudiosantRegistroSerializer(serializers.Serializer):
    grado = serializers.IntegerField()
    nombre_establecimiento = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=8)
    repitente = serializers.BooleanField()


class estudiosantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiosAnt
        fields=(
            'id',
            'grado',
            'nombre_establecimiento',
            'repitente',
            'telefono',
            'estado_estudiosant',
        )
        depth = 2
