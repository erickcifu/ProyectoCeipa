from rest_framework import serializers
from app.models import genero

class generoRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = genero
        fields = (
            'genero',
        )

class generoSerializer(serializers.ModelSerializer):
    class Meta:
        model = genero
        fields=(
        'id',
        'genero',
        'estado_genero',
        )
