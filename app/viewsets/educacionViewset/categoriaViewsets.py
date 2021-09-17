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

from app.models.educacion_model.categoriaModelo import Categoria
from app.serializer.educacion_serializer.categoriaSerializer import categoriaRegistroSerializer, categoriaSerializer


class CategoriaViewset(viewsets.ModelViewset):
    queryset = Categoria.objects.filter(estado_categoria=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_categoria","estado_categoria")
    search_fields = ("nombre_categoria","estado_categoria")
    orderinf_fields = ("nombre_categoria","estado_categoria")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return categoriaSerializer
        else:
            return categoriaRegistroSerializer
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
            serializer = categoriaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    Categoria.objects.create(
                    nombre_categoria = data.get("nombre_categoria"),
                    descripcion_categoria = data.get("descripcion_categoria"),
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
            serializer = categoriaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    categorias= Categoria.objects.get(pk = pk)
                    categorias.nombre_categoria = data.get("nombre_categoria"))
                    categoria.descripcion_categoria = data.get("descripcion_categoria")
                    categoria.save()

                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)