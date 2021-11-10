from django.views import generic
from .mixin import IsEquipoTecnicoSocioProductivoMixin
class HomeEquipoSocioproductivo(IsEquipoTecnicoSocioProductivoMixin,generic.TemplateView):
    template_name = 'equipoSocioproductivo/base.html'