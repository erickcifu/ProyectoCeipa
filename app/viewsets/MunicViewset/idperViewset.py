from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from app.models import IdiomaPersona
from app.forms import IdPerForm

class IdPerView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = IdiomaPersona
    template_name = 'municipalizacion/idper_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class IdPerNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = IdiomaPersona
    template_name = 'municipalizacion/idper_form.html'
    context_object_name = "obj"
    form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:idper_list")
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 7 or user == 8:
                return [self.template_name]
            elif user == 9:
                return ["equipoMunicipal/idper_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 9:
            return redirect('municipalizacion:home_equipo_municipal')
        return redirect("municipalizacion:idper_list")

class IdPerEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = IdiomaPersona
    template_name = "municipalizacion/idper_form.html"
    context_object_name = "obj"
    form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:idper_list")
    login_url = 'app:login'

class IdPerDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = IdiomaPersona
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:idper_list")
