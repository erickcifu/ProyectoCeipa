from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.models import AspectosSalud
from app.forms import AspectosSaludForm
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

class AspectosSaludView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = AspectosSalud
    template_name = 'socioproductivo/aspectos_salud_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AspectosSaludNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = AspectosSalud
    template_name = "socioproductivo/aspectos_salud_form.html"
    context_object_name = "obj"
    form_class = AspectosSaludForm
    success_url = reverse_lazy("socioproductivo:aspectos_salud_list")
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
                return ["equipoSocioproductivo/aspectos_salud_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:aspectos_salud_list")

class AspectosSaludEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = AspectosSalud
    template_name = "socioproductivo/aspectos_salud_form.html"
    context_object_name = "obj"
    form_class = AspectosSaludForm
    success_url = reverse_lazy("socioproductivo:aspectos_salud_list")
    login_url = 'app:login'

class AspectosSaludDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = AspectosSalud
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:aspectos_salud_list")
