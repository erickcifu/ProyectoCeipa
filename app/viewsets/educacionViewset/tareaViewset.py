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

from app.models.educacion_model.tarea import tarea
from app.models.educacion_model.personalEducativo import personalEducativo
from app.models.educacion_model.ciclo_grado_curso import Ciclo_grado_curso
from app.serializer.educacion_serializer.tareaSerializer import tareaRegistroSerializer, tareaSerializer

class TareaViewset(viewsets.ModelViewset):
    queryset = tarea.objects.filter(estado_tarea=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("titulo_tarea","estado_tarea")
    search_fields = ("titulo_tarea","estado_tarea")
    orderinf_fields = ("titulo_tarea","estado_tarea")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return tareaSerializer
        else:
            return tareaRegistroSerializer
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
            serializer = tareaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    maestro = personalEducativo.objects.get(pk=data.get("personalEducativo"))
                    ciclo_grado_curso = Ciclo_grado_curso.objects.get(pk=data.get("ciclo_grado_curso"))
                    tarea.objects.create(
                        titulo_tarea = data.get("titulo_tarea"),
                        descripcion_tarea = data.get("descripcion_tarea"),
                        maestro = maestro,
                        ciclo_grado_curso = ciclo_grado_curso,
                        nota_tarea = data.get("nota_tarea"),
                        fecha_entrega = data.get("fecha_entrega"),
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
            serializer = tareaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    tarea = tarea.objects.get(pk = pk)
                    tarea.titulo_tarea = data.get("titulo_tarea")
                    tarea.descripcion_tarea = data.get("descripcion_tarea")
                    tarea.maestro = personalEducativo.objects.get("personalEducativo")
                    tarea.ciclo_grado_curso = Ciclo_grado_curso.objects.get("ciclo_grado_curso")
                    tarea.nota_tarea = data.get("nota_tarea")
                    tarea.fecha_entrega = data.get("fecha_entrega")
                    tarea.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
