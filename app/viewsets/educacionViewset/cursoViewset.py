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

from app.models.educacion_model.curso import Curso
from app.models.educacion_model.grado import Grado
from app.serializer.educacion_serializer.cursoSerializer import cursoRegistroSerializer, cursoSerializer

class CursoViewset(viewsets.ModelViewset):
    queryset = Curso.objects.filter(estado_curso=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_curso","estado_curso")
    search_fields = ("nombre_curso","estado_curso")
    orderinf_fields = ("nombre_curso","estado_curso")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return cursoSerializer
        else:
            return cursoRegistroSerializer

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
            serializer = cursoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    grado = Grado.objects.get(pk=data.get("grado"))
                    Curso.objects.create(
                        nombre_curso = data.get("nombre_curso"),
                        descripcion_curso = data.get("descripcion_curso"),
                        grado = grado,
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
            serializer = cursoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    curso = Curso.objects.get(pk = pk)
                    curso.nombre_curso = data.get("nombre_curso")
                    curso.descripcion_curso = data.get("descripcion_curso")
                    curso.grado = Grado.objects.get(pk=data.get("grado"))
                    curso.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)