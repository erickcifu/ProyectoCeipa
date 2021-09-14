from rest_framework import serializer
from app.models.educacion_model.idioma import idioma

class idiomaRegistroSerializer(serializer.serializer):
    nombre_idioma = serializers.CharField()

class idiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = centro_educativo
        fields=(
        'id',
        'nombre_idioma',
        'descripcion_idioma',
        'estado_idioma',
        )
