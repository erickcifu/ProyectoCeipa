from rest_framework import serializers
from .app.models.educacion_model.tipo_muro import Tipo_muro


class Tipo_muroRegistroSerializer(serializer.ModelSerializer):
    tipo_muro = serializers.CharField()

class Tipo_muroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_muro
        fields = (
            'id',
            'tipo_muro',
            'descripcion_muro',
            'estado_muro',
            )
        depth = 2