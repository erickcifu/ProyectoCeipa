from rest_framework import serializers
from app.models import religion

class religionRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = religion
        fields = (
            'nombre_religion',
            )

class religionSerializer(serializers.ModelSerializer):
    class Meta:
        model = religion
        fields=(
            'id',
            'nombre_religion',
            'estado_religion',
        )
        depth = 2
