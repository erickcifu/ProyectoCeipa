from rest_framework import serializer
from app.models.educacion_model.municipioModelo import municipio

class municipioRegistroSerializer(serializer.serializer):
    dep = serializers.IntegerField()
    nombre_municipio = serializers.CharField()


class MuniSerializer(serializers.ModelSerializer):
    class Meta:
        model = municipio
        fields=(
        'id',
        'dep',
        'nombre_municipio',
        'estado_municipio',
        )
        depth = 2
