from rest_framework import serializers
from app.models import municipio

class municipioRegistroSerializer(serializers.Serializer):
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
