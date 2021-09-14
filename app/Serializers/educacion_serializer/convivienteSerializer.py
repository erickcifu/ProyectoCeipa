from rest_framework import serializers
from .app.models.educacion_model.conviviente import Conviviente


class ConvivienteRegistroSerializer(serializer.ModelSerializer):
    class Meta:
        model = Conviviente
        fields = (
            'nombres_conviviente',
        )

class ConvivienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conviviente
        fields = (
            'id', 
            'nombres_conviviente', 
            'apellidos_conviviente', 
            'estado_conviviente',
            'fecha_nacimiento'
            )