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

from app.models.educacion_model.servicio_agua import Servicio_Agua
from app.serializer.educacion_serializer.servicio_aguaSerializer import Servicio_aguaRegistroSerializer, Servicio_aguaSerializer

class Servicio_aguaViewset(viewsets.ModelViewset):
    queryset = Servicio_Agua.objects.filter(estado_agua=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("servicio_agua", "estado_agua")
    search_fields = ("servicio_agua", "estado_agua")
    orderinf_fields = ("servicio_agua", "estado_agua")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Servicio_aguaSerializer
        else:
            return Servicio_aguaRegistroSerializer
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
            serializer = Servicio_aguaRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Servicio_Agua.objects.create(
                        servicio_agua = data.get("servicio_agua"),
                        descripcion_servicio_agua = data.get("descripcion_servicio_agua"),
                        estado_agua = data.get("estado_agua"),
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
            serializer = Servicio_aguaRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    servicio = Servicio_Agua.objects.get(pk = pk)
                    servicio.servicio_agua = data.get("servicio_agua")
                    servicio.descripcion_servicio_agua = data.get("descripcion_servicio_agua")
                    servicio.estado_agua = data.get("estado_agua")
                    servicio.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST