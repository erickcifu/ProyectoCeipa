from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from app.models import Encargado
from app.forms import EncargadoForm

class EncargadoView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = Encargado
    template_name = 'socioproductivo/Encargado_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EncargadoNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = Encargado
    template_name = "socioproductivo/Encargado_form.html"
    context_object_name = "obj"
    form_class = EncargadoForm
    success_url = reverse_lazy("socioproductivo:Encar_list")
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 10 or user == 11:
                return [self.template_name]
            elif user == 12:
                return ["equipoSocioproductivo/Encargado_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:Encar_list")

class EncargadoEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = Encargado
    template_name = "socioproductivo/Encargado_form.html"
    context_object_name = "obj"
    form_class = EncargadoForm
    success_url = reverse_lazy("socioproductivo:Encar_list")
    login_url = 'app:login'

class EncargadoDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = Encargado
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:Encar_list")
