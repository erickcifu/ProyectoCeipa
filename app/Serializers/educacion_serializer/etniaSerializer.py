from rest_framework import serializer
from app.models.educacion_model.etnia import etnia

class EtniaRegistroSerializer(serializer.ModelSerializer):
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
