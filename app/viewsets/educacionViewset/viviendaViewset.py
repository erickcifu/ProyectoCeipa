import json
from django.db import transaction
from django.core.files import File
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings

from app.models import vivienda
from app.models import Tipo_techo
from app.models import Categoria
from app.models import Tipo_piso
from app.models import Servicio_Agua
from app.models import Alumno
from app.serializer import viviendaRegistroSerializer, viviendaSerializer


class ViviendaViewset(viewsets.ModelViewSet):
    queryset = vivienda.objects.filter(estado_vivienda=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("cantidad_personas","estado_vivienda")
    search_fields = ("cantidad_personas","estado_vivienda")
    orderinf_fields = ("cantidad_personas","estado_vivienda")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return viviendaSerializer
        else:
            return viviendaRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = viviendaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    techo = Tipo_techo.objects.get(pk = data.get("techo"))
                    categoria = categoriaModel.objects.get(pk = data.get("categoria"))
                    tipo_piso = tipopisoModel.objects.get(pk = data.get("tipo_piso"))
                    servicio = servicio_agua.objects.get(pk = data.get("servicio"))
                    alumno = Alumno.objects.get(pk = data.get("alumno"))
                    vivienda.objects.create(
                        cantidad_personas = data.get("cantidad_personas"),
                        cantidad_ambientes = data.get("cantidad_ambientes"),
                        energia_electrica = data.get("energia_electrica"),
                        servicio_sanitario = data.get("servicio_sanitario"),
                        letrina = data.get("letrina"),
                        techo = techo,
                        categoria = categoria,
                        piso = tipo_piso,
                        servicio = servicio,
                        estudiante = alumno,
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = viviendaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    vivienda = vivienda.objects,get(pk = pk)
                    vivienda.cantidad_personas = data.get("cantidad_personas")
                    vivienda.cantidad_ambientes = data.get("cantidad_ambientes")
                    vivienda.energia_electrica = data.get("energia_electrica")
                    vivienda.servicio_sanitario = data.get("servicio_sanitario")
                    vivienda.letrina = data.get("letrina")
                    vivienda.techo = Tipo_techo.objects.get("techo")
                    vivienda.categoria = categoria.objects.get("categoria")
                    vivienda.piso = Tipo_piso.objects.get("piso")
                    vivienda.servicio = Servicio_Agua.objects.get("servicio")
                    vivienda.estudiante = Alumno.objects.get("estudiante")
                    vivienda.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
