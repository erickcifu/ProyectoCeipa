from rest_framework import serializers
from app.models import Categoria

class categoriaRegistroSerializer(serializers.Serializer):
    nombre_categoria = serializers.CharField()


class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields=(
        'id',
        'nombre_categoria',
        'descripcion_categoria',
        'estado_categoria',
        )
