from rest_framework import serializers
from .app.models.educacion_model.conviviente import Conviviente


class ConvivienteRegistroSerializer(serializer.ModelSerializer):
    vivienda = serializers.IntegerField()
    parentesco = serializers.IntegerField()
    nombres_conviviente = serializers.CharField()
    apellidos_conviviente = serielizers.CharField()
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