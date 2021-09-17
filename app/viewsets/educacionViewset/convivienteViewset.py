import json
from django.core.files import File
from django_filters.rest_framework import djangoFilterBackend
from rest_framework import status, filters, viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings

from app.models.educacion_model.conviviente import Conviviente
from app.serializer.educacion_serializer.convivienteSerializer import ConvivienteRegistroSerializer, ConvivienteSerializer
from app.models.educacion_model.vivienda import vivienda
from app.models.educacion_model.parentesco import Parentesco

class ConvivienteViewset(viewsets.ModelViewset):
    queryset = Conviviente.objects.filter(estado_conviviente=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("vivienda__cantidad_personas", "Parentesco__nombre_parentesco", "estado_conviviente")
    search_fields = ("vivienda__cantidad_personas", "Parentesco__nombre_parentesco", "estado_conviviente")
    orderinf_fields = ("vivienda__cantidad_personas", "Parentesco__nombre_parentesco", "estado_conviviente")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ConvivienteSerializer
        else:
            return ConvivienteRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
        else:
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

"""******************** CREATE *****************************"""
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = ConvivienteRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    vivienda = vivienda.objects.get(pk=data.get("vivienda"))
                    Parentesco = Parentesco.objects.get(pk=data.get("Parentesco"))
                    Conviviente.objects.create(
                        vivienda = vivienda,
                        Parentesco = Parentesco,
                        nombres_conviviente = data.get("nombres_conviviente"),
                        apellidos_conviviente = data.get("apellidos_conviviente"),
                        estado_conviviente = data.get("estado_conviviente"),
                        fecha_nacimiento = data.get("fecha_nacimiento"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

"""******************** UPDATE *****************************"""
    def update(self,request,pk=none):
        try:
            data = request.data
            serializer = ConvivienteRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    conviviente = Conviviente.objects.get(pk = pk)
                    conviviente.vivienda = vivienda.objects.get(pk=data.get("tarea"))
                    conviviente.parentesco = Parentesco.objets.get(pk=data.get("alumno"))
                    conviviente.nombres_conviviente = data.get("nombres_conviviente")
                    conviviente.apellidos_conviviente = data.get("apellidos_conviviente")
                    conviviente.fecha_nacimiento = data.get('fecha_nacimiento')
                    conviviente.estado_conviviente = data.get("estado_conviviente")
                    conviviente.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST