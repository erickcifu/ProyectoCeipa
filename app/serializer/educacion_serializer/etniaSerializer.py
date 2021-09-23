from rest_framework import serializers
from app.models import etnia

class EtniaRegistroSerializer(serializers.Serializer):
    nombre_etnia = serializers.CharField()

class EtniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = etnia
        fields = (
            'id',
            'nombre_etnia',
            'descripcion_etnia',
            'estado_etnia',
            )
        depth = 2
