from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.viewsets.users.forms.FormUser import UserFormEquipoSocioproductivoAsisenteSocioproductivo
from django.contrib.auth.models import User
from django.db.models import F
from .mixin import IsCoordinadorSocioProductivoMixin

class CrearAsistenteSocioproductivoEquipoSocio(IsCoordinadorSocioProductivoMixin,generic.CreateView):
    model = User
    form_class = UserFormEquipoSocioproductivoAsisenteSocioproductivo
    template_name = 'coordinadorSocioproductivo/CrearUsuario.html'
    success_url = reverse_lazy('socioproductivo:listar_usuarios_socioproductivos')

class ListarAsistenteSocioproductivoEquipoSocio(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = User
    context_object_name = "obj"
    template_name = 'coordinadorSocioproductivo/listarUsuarios.html'

    def get_queryset(self):
        return User.objects.filter(is_active=True, user_profile__rol_id__in=[10,11,12]).annotate(cargo=F('user_profile__rol__nombre_rol'))
