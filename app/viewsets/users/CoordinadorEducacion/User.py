from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.viewsets.users.forms.FormUser import UserFormAsignarRolesCoordinadorEducacion
from django.contrib.auth.models import User
from django.db.models import F
from .mixin import IsCoordinadorEducacionMixin

class CrearAsistenteMaestroDirectorCentro(IsCoordinadorEducacionMixin,generic.CreateView):
    model = User
    form_class = UserFormAsignarRolesCoordinadorEducacion
    template_name = 'coordinadorEducacion/CrearUsuario.html'
    success_url = reverse_lazy('educacion:listar_maestro_director_centro')

class ListarAsistentesMaestrosDirectorCentro(IsCoordinadorEducacionMixin, generic.ListView):
    model = User
    context_object_name = "obj"
    template_name = 'coordinadorEducacion/listarUsuarios.html'

    def get_queryset(self):
        return User.objects.filter(is_active=True, user_profile__rol_id__in=[1,2,5,6]).annotate(cargo=F('user_profile__rol__nombre_rol'))
