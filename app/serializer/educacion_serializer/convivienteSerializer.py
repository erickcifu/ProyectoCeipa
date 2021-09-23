from rest_framework import serializers
from app.models import Conviviente

class ConvivienteRegistroSerializer(serializers.Serializer):
    vivienda = serializers.IntegerField()
    parentesco = serializers.IntegerField()
    nombres_conviviente = serializers.CharField()
    apellidos_conviviente = serializers.CharField()
    estado_conviviente = serializers.BooleanField()
    fecha_nacimiento = serializers.DateField()

class ConvivienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conviviente
        fields = (
            'id',
            'vivienda',
            'parentesco',
            'nombres_conviviente',
            'apellidos_conviviente',
            'estado_conviviente',
            'fecha_nacimiento',
        )
        depth = 2
