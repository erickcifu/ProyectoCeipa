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

from app.models.educacion_model import ocupacion
from app.serializer.educacionSerializer import ocupacionRegistroSerializer, ocupacionSerializer
<<<<<<< HEAD
=======
#adsdiasdas
>>>>>>> 67230c60d8d899aab60e997b6c1ee50c01e41f1b
