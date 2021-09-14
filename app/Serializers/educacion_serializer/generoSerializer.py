from rest_framework import serializer
from app.models.educacion_model.genero import genero

class generoRegistroSerializer(serializer.ModelSerializer):
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
