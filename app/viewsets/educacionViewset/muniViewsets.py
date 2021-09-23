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

from app.models import municipio
from app.serializer import municipioRegistroSerializer, MuniSerializer
from app.models import departamento

class MuniViewset(viewsets.ModelViewSet):
    queryset = municipio.objects.filter(estado_municipio=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_municipio","estado_municipio")
    search_fields = ("nombre_municipio","estado_municipio")
    ordering_fields = ("nombre_municipio","estado_municipio")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return MuniSerializer
        else:
            return municipioRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            serializer = municipioRegistroSerializer(data = data)
            with transaction.atomic():#detiene procesos si hay mas
                if serializer.is_valid():
                    dep = departamento.objects.get(pk=data.get('dep'))
                    municipio.objects.create(
                    dep = dep,
                    nombre_municipio = data.get("nombre_municipio"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = municipioRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    municipio = municipio.objects.get(pk = pk)
                    municipio.dep = departamento.objects.get(pk=data.get("departamento"))
                    municipio.nombre_municipio = data.get("nombre_municipio")
                    municipio.save()

                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
