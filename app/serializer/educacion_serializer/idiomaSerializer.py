from rest_framework import serializers
from app.models import idioma

class idiomaRegistroSerializer(serializers.Serializer):
    nombre_idioma = serializers.CharField()

class idiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = idioma
        fields=(
            'id',
            'nombre_idioma',
            'descripcion_idioma',
            'estado_idioma',
        )
