from django.views import generic
from app.models.educacion_model.centro_educativo import centro_educativo
from app.viewsets.users.directorCentro.mixin import IsDirectorCentroMixin

class HomeDirectorCentro(IsDirectorCentroMixin,generic.TemplateView):
    template_name = 'directorCentro/base.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user:
            context['centro_educativo'] = centro_educativo.objects.filter(c_educativo__personal__perfile = user.user_profile).first()
        return context
