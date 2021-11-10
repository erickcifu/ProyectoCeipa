from django.views import generic
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin

class HomeCoordinadorSocioproductivo(IsCoordinadorSocioProductivoMixin,generic.TemplateView):
    template_name = 'app/HomeSocioproductivo.html'
