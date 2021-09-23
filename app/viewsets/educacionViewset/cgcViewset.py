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

from app.models import Ciclo_grado_curso
from app.models import personalEducativo
from app.models import Curso
from app.models import Ciclo_grado
from app.serializer import cgcRegistroSerializer, cgcSerializer

class CgcViewset(viewsets.ModelViewSet):
    queryset = Ciclo_grado_curso.objects.filter(estado_cgc=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("curso__nombre_curso","estado_cgc")
    search_fields = ("curso__nombre_curso","estado_cgc")
    ordering_fields = ("curso__nombre_curso","estado_cgc")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return cgcSerializer
        else:
            return cgcRegistroSerializer

    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = cgcRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    maestro = personalEducativo.objects.get(pk=data.get("maestro"))
                    curso = Curso.objects.get(pk=data.get("curso"))
                    ciclo_grado = Ciclo_grado.objects.get(pk=data.get("ciclo_grado"))
                    Ciclo_grado_curso.objects.create(
                        maestro = maestro,
                        curso = curso,
                        ciclo_grado = ciclo_grado,
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = cgcRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    ciclo_grado_curso = Ciclo_grado_curso.objects.get(pk = pk)
                    ciclo_grado_curso.maestro = personalEducativo.objects.get(pk=data.get("maestro"))
                    ciclo_grado_curso.curso = Curso.objects.get(pk=data.get("curso"))
                    ciclo_grado_curso.ciclo_grado = Ciclo_grado.objects.get(pk=data.get("ciclo_grado"))
                    ciclo_grado_curso.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
