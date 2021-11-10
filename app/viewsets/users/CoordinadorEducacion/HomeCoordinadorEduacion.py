from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin

class HomeCoordinadorEducacion(IsCoordinadorEducacionMixin,generic.TemplateView):
    template_name = 'base/base3.html'
