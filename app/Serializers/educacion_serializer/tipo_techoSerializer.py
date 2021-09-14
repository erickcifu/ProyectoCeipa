from rest_framework import serializers
from .app.models.educacion_model.tipo_techo import Tipo_techo


class Tipo_techoRegistroSerializer(serializer.ModelSerializer):
    class Meta:
        model = Tipo_techo
        fields = (
            'tipo_techo',
        )

class Tipo_techoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_techo
        fields = (
            'id', 
            'tipo_techo', 
            'descripcion_techo', 
            'estado_techo'
            )