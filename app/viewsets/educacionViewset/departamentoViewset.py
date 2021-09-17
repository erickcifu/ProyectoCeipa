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

from app.models.educacion_model.departamento import departamento
from app.serializer.educacion_serializer.departamentoSerializer import departamentoRegistroSerializer, departamentoSerializer

class DepartamentoViewset(viewsets.ModelViewset):
    queryset = tarea.objects.filter(estado_departamento=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_departamento","estado_departamento")
    search_fields = ("nombre_departamento","estado_departamento")
    orderinf_fields = ("nombre_departamento","estado_departamento")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return departamentoSerializer
        else:
            return departamentoRegistroSerializer
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
            serializer = departamentoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    departamento.objects.create(
                        nombre_departamento = data.get("nombre_departamento")
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
            serializer = departamentoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    departamento = departamento.objects.get(pk = pk)
                    departamento.nombre_departamento = data.get("nombre_departamento")
                    departamento.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)