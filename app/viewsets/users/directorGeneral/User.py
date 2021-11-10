from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.viewsets.users.forms.FormUser import UserFormCoordinadorGeneral, UserFormDirectorOAsistenteGeneral
from django.contrib.auth.models import User
from django.db.models import F
from .mixin import IsDirectorGeneralMixin

class CrearCoordinador(IsDirectorGeneralMixin,generic.CreateView):
    model = User
    form_class = UserFormCoordinadorGeneral
    
    template_name = 'directorGeneral/CrearCoordinador.html'
    success_url = reverse_lazy('educacion:listar_coordinador')

class ListarCoordinadores(IsDirectorGeneralMixin, generic.ListView):
    model = User
    context_object_name = "obj"
    template_name = 'directorGeneral/listarUsuarios.html'

    def get_queryset(self):
        return User.objects.filter(is_active=True, user_profile__rol_id__in=[1,2,7,8,10,11]).annotate(cargo=F('user_profile__rol__nombre_rol'))


class CrearDirectorGeneral(IsDirectorGeneralMixin, generic.CreateView):
    model = User
    form_class = UserFormDirectorOAsistenteGeneral
    template_name = 'directorGeneral/CrearDirectorGeneral.html'
    success_url = reverse_lazy('educacion:listar_coordinador')