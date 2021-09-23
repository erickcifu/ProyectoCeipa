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

from app.models import Centropersona
from app.serializer import centropersonaRegistroSerializer,  centropersonaSerializer
from app.models import centro_educativo
from app.models import personalEducativo

class CentroPViewset(viewsets.ModelViewSet):
    queryset = Centropersona.objects.filter(estado_centropersona = True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("centro_Educativo__nombre_centro","estado_centropersona")
    search_fields = ("centro_Educativo__nombre_centro","estado_centropersona")
    ordering_fields = ("centro_Educativo__nombre_centro","estado_centropersona")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return  centropersonaSerializer
        else:
            return centropersonaRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            serializer = centropersonaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    centro_Educativo = centro_educativo.objects.get(pk=data.get("centro_Educativo"))
                    personal = personalEducativo.objects.get(pk=data.get('personal'))
                    Centropersona.objects.create(
                    centro_Educativo = centro_Educativo,
                    personal = personal
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
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
