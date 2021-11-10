from django.views import generic
from app.viewsets.users.EquipoTecMunicipal.mixin import IsEquipoTecnicoMunicipalMixin

class HomeEquipoMunicipal(IsEquipoTecnicoMunicipalMixin,generic.TemplateView):
    template_name = 'EquipoMunicipal/municipalizacion.html'
