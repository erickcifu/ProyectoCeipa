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

from app.models import Ciclo_grado
from app.models import Grado
from app.models import Ciclo
from app.models import seccion
from app.serializer import cgRegistroSerializer, cgSerializer

class CgViewset(viewsets.ModelViewSet):
    queryset = Ciclo_grado.objects.filter(estado_cg=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("grado__nombre_grado","ciclo__anio")
    search_fields = ("grado__nombre_grado","ciclo__anio")
    ordering_fields = ("grado_nombre_grado","ciclo__anio")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return cgSerializer
        else:
            return cgRegistroSerializer

    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = cgRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    grado = Grado.objects.get(pk=data.get("grado"))
                    ciclo = Ciclo.objects.get(pk=data.get("ciclo"))
                    seccion = seccion.objects.get(pk=data.get("seccion"))
                    Ciclo_grado.objects.create(
                        grado = grado,
                        ciclo = ciclo,
                        seccion = seccion,
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = cgRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    ciclo_grado = Ciclo_grado.objects.get(pk = pk)
                    ciclo_grado.grado = Grado.objects.get(pk=data.get("grado"))
                    ciclo_grado.ciclo = ciclo = Ciclo.objects.get(pk=data.get("ciclo"))
                    ciclo_grado.seccion = seccion.objects.get(pk=data.get("seccion"))
                    ciclo_grado.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
