from rest_framework import serializer
from app.models.educacion_model.departamento import departamento

class departamentoRegistroSerializer(serializer.ModelSerializer):
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
