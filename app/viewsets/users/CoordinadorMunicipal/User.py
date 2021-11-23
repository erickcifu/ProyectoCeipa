from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import F
from django.shortcuts import redirect
from .mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.forms.FormUser import UserFormEquipoMunicipalAsisenteMunicipal

class CrearEquipoMunicipalYAsistenteMunicipal(IsCoordinadorMunicipalMixin,generic.CreateView):
    model = User
    form_class = UserFormEquipoMunicipalAsisenteMunicipal
    template_name = 'CoordinadorMunicipal/CrearUsuario.html'
    success_url = reverse_lazy('educacion:listar_asistente_equipo_municipal')

class ListarPersonalEquipoMunicipalAsistenteMunicipal(IsCoordinadorMunicipalMixin,generic.ListView):
    model = User
    context_object_name = "obj"
    template_name = 'CoordinadorMunicipal/listarUsuarios.html'

    def get_queryset(self):
        return User.objects.filter(is_active=True, user_profile__rol_id__in=[7,8,9]).annotate(cargo=F('user_profile__rol__nombre_rol'))


class DeleteUserMuni(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = User
    template_name = 'CoordinadorMunicipal/deletemunicip.html'
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:listar_asistente_equipo_municipal")
