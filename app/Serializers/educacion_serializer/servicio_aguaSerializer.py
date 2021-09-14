from rest_framework import serializers
from .app.models.educacion_model.servicio_agua import Servicio_Agua


class Servicio_aguaRegistroSerializer(serializer.ModelSerializer):
    class Meta:
        model = Servicio_Agua
        fields = (
            'servicio_agua',
        )

class Servicio_aguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio_Agua
        fields = (
            'id', 
            'servicio_agua', 
            'descripcion_servicio_agua', 
            'estado_agua'
            )