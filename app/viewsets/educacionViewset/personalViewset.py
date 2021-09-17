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

from app.models.educacion_model.personalEducativo import personalEducativo
from app.serializer.educacion_serializer.personalSerializer import personalRegistroSerializer, personalSerializer

class PersonalViewset(viewsets.ModelViewset):
    queryset = personalEducativo.objects.filter(estado_personal=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre","estado_personal")
    search_fields = ("nombre","estado_personal")
    orderinf_fields = ("nombre","estado_personal")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return personalSerializer
        else:
            return personalRegistroSerializer

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
            serializer = personalRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    personalEducativo.objects.create(
                        nombres = data.get("nombres"),
                        apellidos = data.get("apellidos"),
                        telefono_personal = data.get("telefono_personal"),
                        email_personal = data.get("email_personal"),
                        fechaNac_personal = data.get("fechaNac_personal"),
                        direccion_personal = data.get("direccion_personal"),
                        certificadoRenas_personal = data.get("certificadoRenas_personal"),
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
            serializer = personalRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    personalEducativo = personalEducativo.objects.get(pk=pk)
                    personalEducativo.nombres = data.get("nombres")
                    personalEducativo.apellidos = data.get("apellidos")
                    personalEducativo.telefono_personal = data.get("telefono_personal")
                    personalEducativo.email_personal = data.get("email_personal")
                    personalEducativo.fechaNac_personal = data.get("fechaNac_personal")
                    personalEducativo.direccion_personal = data.get("direccion_personal")
                    personalEducativo.certificadoRenas_personal = data.get("certificadoRenas_personal")
                    personalEducativo.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
