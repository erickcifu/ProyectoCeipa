from rest_framework import serializer
from app.models.educacion_model.categoriaModelo import Categoria

class categoriaRegistroSerializer(serializer.serializer):
    nombre_categoria = serializers.CharField()


class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields=(
        'id',
        'nombre_categoria',
        'descripcion_categoria',
        'estado_categoria',
        )
