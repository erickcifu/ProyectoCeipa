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

from app.models.educacion_model.tipo_muro import Tipo_muro
from app.serializer.educacion_serializer.tipo_techoSerializer import Tipo_muroRegistroSerializer, Tipo_muroSerializer

class Tipo_muroViewset(viewsets.ModelViewset):
    queryset = Tipo_muro.objects.filter(estado_muro=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("tipo_muro", "estado_muro")
    search_fields = ("tipo_muro", "estado_muro")
    orderinf_fields = ("tipo_muro", "estado_muro")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Tipo_muroSerializer
        else:
            return Tipo_muroRegistroSerializer
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
            serializer = Tipo_muroRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Tipo_muro.objects.create(
                        tipo_muro = data.get("tipo_muro"),
                        descripcion_muro = data.get("descripcion_muro"),
                        estado_muro = data.get("estado_muro"),
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
            serializer = Tipo_muroRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    tipomu = Tipo_techo.objects.get(pk = pk)
                    tipomu.tipo_muro = data.get("tipo_muro")
                    tipomu.descripcion_muro = data.get("descripcion_muro")
                    tipomu.estado_muro = data.get("estado_muro")
                    tipomu.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST