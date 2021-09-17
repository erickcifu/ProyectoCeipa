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

from app.models.educacion_model.centro_educativo import centro_educativo
from app.serializer.educacion_serializer.centroSerializer import centroRegistroSerializer, centroSerializer

class CentroViewset(viewsets.ModelViewset):
    queryset = centro_educativo.objects.filter(estado_centro=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_centro","codigo_centro")
    search_fields = ("nombre_centro","codigo_centro")
    orderinf_fields = ("nombre_centro","codigo_centro")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return centroSerializer
        else:
            return centroRegistroSerializer

    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    """******************** CREATE *****************************"""
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = centroRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    centro_educativo.objects.create(
                        nombre_centro = data.get("nombre_centro"),
                        direccion_centro = data.get("direccion_centro"),
                        codigo_centro = data.get("codigo_centro"),
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    """********************** ACTULIZAR ***************************"""
    def update(self,request,pk=none):
        try:
            data = request.data
            serializer = centroRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    centro_educativo = centro_educativo.objects.get(pk = pk)
                    centro_educativo.nombre_centro = data.get("nombre_centro")
                    centro_educativo.direccion_centro = data.get("direccion_centro")
                    centro_educativo.codigo_centro = data.get("codigo_centro")
                    centro_educativo.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
