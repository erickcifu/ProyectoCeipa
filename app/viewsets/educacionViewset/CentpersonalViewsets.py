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

from app.models.educacion_model.centropersonaModel import Centropersona
from app.serializer.educacion_serializer.centropersonaSerializer import centropersonaRegistroSerializer,  centropersonaSerializer
from app.models.educacion_model.centro_Educativo import centro_educativo
from app.models.educacion_model.personalEducativo import personalEducativo

class CentroPViewset(viewsets.ModelViewset):
    queryset = Centropersona.objects.filter(estado_centropersona = True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("centro_Educativo__nombre_centro","estado_centropersona")
    search_fields = ("centro_Educativo__nombre_centro","estado_centropersona")
    orderinf_fields = ("centro_Educativo__nombre_centro","estado_centropersona")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return  centropersonaSerializer
        else:
            return centropersonaRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
        else:
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]
"""******************** Crear *************************************-"""
    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            Centropersona = centropersonaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    centro_Educativo = centro_educativo.objects.get(pk=data.get("centro_educativo"))
                    personal = personalEducativo.objects.get(pk=data.get('personalEducativo'))
                    Centropersona.objects.create(
                    centro_Educativo = centro_Educativo,
                    personal = personal
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
            serializer = centropersonaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    Centropersona = Centropersona.objects.get(pk = pk)
                    Centropersona.centro_Educativo = centro_educativo.objects.get(pk=data.get("centro_educativo"))
                    Centropersona.personal = personalEducativo.objects.get(pk=data.get("personalEducativo"))
                    Centropersona.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
