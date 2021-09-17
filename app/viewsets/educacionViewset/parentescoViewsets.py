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

from app.models.educacion_model.parentesco import Parentesco
from app.serializer.educacion_serializer.parentescoSerializer import ParentescoRegistroSerializer, ParentescoSerializer

class ParentescoViewset(viewsets.ModelViewset):
    queryset = Parentesco.objects.filter(estado_parentesco=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_parentesco", "estado_parentesco")
    search_fields = ("nombre_parentesco", "estado_parentesco")
    orderinf_fields = ("nombre_parentesco", "estado_parentesco")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ParentescoSerializer
        else:
            return ParentescoRegistroSerializer
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
            serializer = ParentescoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Parentesco.objects.create(
                        nombre_parentesco = data.get("nombre_parentesco"),
                        descripcion_parentesco = data.get("descripcion_parentesco"),
                        estado_parentesco = data.get("estado_parentesco"),
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
            serializer = ParentescoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Parentesco = Parentesco.objects.get(pk = pk)
                    Parentesco.nombre_parentesco = data.get("nombre_parentesco")
                    Parentesco.descripcion_parentesco = data.get("descripcion_parentesco")
                    Parentesco.estado_parentesco = data.get("estado_parentesco")
                    Parentesco.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST
