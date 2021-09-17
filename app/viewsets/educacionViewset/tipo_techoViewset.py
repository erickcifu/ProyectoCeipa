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

from app.models.educacion_model.tipo_techo import Tipo_techo
from app.serializer.educacion_serializer.tipo_techoSerializer import Tipo_techoRegistroSerializer, Tipo_techoSerializer

class Tipo_techoViewset(viewsets.ModelViewset):
    queryset = Tipo_techo.objects.filter(estado_techo=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("tipo_techo", "estado_techo")
    search_fields = ("tipo_techo", "estado_techo")
    orderinf_fields = ("tipo_techo", "estado_techo")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Tipo_techoSerializer
        else:
            return Tipo_techoRegistroSerializer
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
            serializer = Tipo_techoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Tipo_techo.objects.create(
                        tipo_techo = data.get("tipo_techo"),
                        descripcion_techo = data.get("descripcion_techo"),
                        estado_techo = data.get("estado_techo"),
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
            serializer = Tipo_techoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    tipote = Tipo_techo.objects.get(pk = pk)
                    tipote.tipo_techo = data.get("tipo_techo")
                    tipote.descripcion_techo = data.get("descripcion_techo")
                    tipote.estado_techo = data.get("estado_techo")
                    tipote.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST