"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from app import viewsets


router = DefaultRouter()

urlpatterns = [
path('app',include(router.urls)),
url(r"app/token",obtain_auth_token, name="app-token"),
path('api-auth/',include('rest_framework.urls')),
]
"""
