from rest_framework import serializers
from .app.models.educacion_model.parentesco import Parentesco

class ParentescoRegistroSerializer(serializer.ModelSerializer):
    nombre_parentesco = serializers.CharField()

class ParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parentesco
        fields = (
            'id',
            'nombre_parentesco',
            'descripcion_parentesco',
            'estado_parentesco',
            )
        depth = 2