from rest_framework import serializers
from .app.models.educacion_model.servicio_agua import Servicio_Agua


class Servicio_aguaRegistroSerializer(serializer.ModelSerializer):
    servicio_agua = serializers.CharField()

class Servicio_aguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio_Agua
        fields = (
            'id',
            'servicio_agua',
            'descripcion_servicio_agua',
            'estado_agua',
            )
        depth = 2