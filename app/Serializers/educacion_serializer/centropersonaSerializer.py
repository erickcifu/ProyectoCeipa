from rest_framework import serializer
from app.models.educacion_model.centropersonaModel import Centropersona

class centropersonaRegistroSerializer(serializer.serializer):
    centro_Educativo = serializers.IntegerField()
    personal = serializers.IntegerField()


class centropersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centropersona
        fields=(
        'id',
        'centro_Educativo',
        'personal',
        'estado_centropersona',
        )
        depth = 2
