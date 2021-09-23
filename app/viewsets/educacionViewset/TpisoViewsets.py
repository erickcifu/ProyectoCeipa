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

from app.models import Tipo_piso
from app.serializer import tipopisoRegistroSerializer, tipopisoSerializer

class TpisoViewset(viewsets.ModelViewSet):
    queryset = Tipo_piso.objects.filter(estado_tipopiso=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("tipo_piso","estado_tipopiso")
    search_fields = ("tipo_piso","estado_tipopiso")
    orderinf_fields = ("tipo_piso","estado_tipopiso")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return tipopisoSerializer
        else:
            return tipopisoRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            serializer = tipopisoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    seccion.objects.create(
                    tipo_piso = data.get("tipo_piso"),
                    descripcion_tipopiso = data.get("descripcion_tipopiso")
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = tipopisoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    Tipo_piso= Tipo_piso.objects.get(pk = pk)
                    tipo_piso.tipo_piso = data.get("Tipo_piso")
                    tipo_piso.save()

                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
