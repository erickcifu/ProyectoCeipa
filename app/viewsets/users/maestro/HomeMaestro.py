from django.views import generic
from app.viewsets.users.maestro.mixin import IsMaestroMixin

class HomeMaestro(IsMaestroMixin,generic.TemplateView):
    template_name = 'maestro/base.html'
