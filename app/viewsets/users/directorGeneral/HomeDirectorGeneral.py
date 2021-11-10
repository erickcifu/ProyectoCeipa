from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class HomeDirectorGeneral(LoginRequiredMixin,generic.TemplateView):
    template_name = 'directorGeneral/home.html'
