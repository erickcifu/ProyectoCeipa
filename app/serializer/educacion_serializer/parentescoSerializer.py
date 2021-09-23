from rest_framework import serializers
from app.models import Parentesco

class ParentescoRegistroSerializer(serializers.Serializer):
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
