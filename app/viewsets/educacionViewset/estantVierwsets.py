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

from app.models import EstudiosAnt
from app.serializer import estudiosantRegistroSerializer, estudiosantSerializer
from app.models import grados

class estuantoViewset(viewsets.ModelViewSet):
    queryset = EstudiosAnt.objects.filter(estado_estudiosant=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_establecimiento","estado_estudiosant")
    search_fields = ("nombre_establecimiento","estado_estudiosant")
    ordering_fields = ("nombre_establecimiento","estado_estudiosant")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return estudiosantSerializer
        else:
            return estudiosantRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            serializer = estudiosantRegistroSerializer(data = data)
            with transaction.atomic():#detiene procesos si hay mas
                if serializer.is_valid():
                    grado = grados.objects.get(pk=data.get('grado'))
                    EstudiosAnt.objects.create(
                    grado = grado,
                    nombre_establecimiento = data.get("nombre_establecimiento"),
                    repitente = data.get("repitente"),
                    telefono = data.get("telefono"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = estudiosantRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    EstudiosAnt = EstudiosAnt.objects.get(pk = pk)
                    EstudiosAnt.grado = grados.objects.get(pk=data.get("grados"))
                    EstudiosAnt.nombre_establecimiento = data.get("nombre_establecimiento")
                    EstudiosAnt.repitente = data.get("repitente")
                    EstudiosAnt.telefono = data.get("telefono")
                    EstudiosAnt.save()

                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
