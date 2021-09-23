from rest_framework import serializers
from app.models import departamento

class departamentoRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = departamento
        fields = (
            'nombre_departamento',
        )

class departamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = departamento
        fields=(
        'id',
        'nombre_departamento',
        'estado_departamento',
        )
