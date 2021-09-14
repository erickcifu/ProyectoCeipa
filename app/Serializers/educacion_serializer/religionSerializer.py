from rest_framework import serializer
from app.models.educacion_model.religion import religion

class religionRegistroSerializer(serializer.ModelSerializer):
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
