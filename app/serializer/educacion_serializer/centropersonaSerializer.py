from rest_framework import serializers
from app.models import Centropersona

class centropersonaRegistroSerializer(serializers.Serializer):
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
