from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from app.models import ElectVivienda
from app.forms import ElectvivForm

class ElectvivView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = ElectVivienda
    template_name = 'socioproductivo/electviv_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ElectvivNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = ElectVivienda
    template_name = "socioproductivo/electviv_form.html"
    context_object_name = "obj"
    form_class = ElectvivForm
    success_url = reverse_lazy("socioproductivo:electviv_list")
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
                return ["equipoSocioproductivo/electviv_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:electviv_list")

class ElectvivEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = ElectVivienda
    template_name = "socioproductivo/electviv_form.html"
    context_object_name = "obj"
    form_class = ElectvivForm
    success_url = reverse_lazy("socioproductivo:electviv_list")
    login_url = 'app:login'

class ElectvivDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = ElectVivienda
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:electviv_list")
