from rest_framework import serializer
from app.models.educacion_model.vivienda import vivienda

class viviendaRegistroSerializer(serializer.serializer):
    cantidad_personas = serializers.IntegerField()
    cantidad_ambientes = serializers.IntegerField()
    energia_electrica = serializers.BooleanField(default=False)
    servicio_sanitario = serializers.BooleanField(default=False)
    letrina = serializers.BooleanField(default=False)
    techo = serializers.IntegerField()
    categoria = serializers.IntegerField()
    piso = serializers.IntegerField()
    servicio = serializers.IntegerField()
    estudiante = serializers.IntegerField()

class viviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields=(
        'id',
        'cantidad_personas',
        'cantidad_ambientes',
        'energia_electrica',
        'servicio_sanitario',
        'letrina',
        'techo',
        'categoria',
        'piso',
        'servicio',
        'estudiante',
        'estado_vivienda',
        )
        depth = 2
