from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from app.models import Area
from app.forms import AreaForm

class AreaView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Area
    template_name = 'municipalizacion/area_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AreaNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = Area
    template_name = 'municipalizacion/area_form.html'
    context_object_name = "obj"
    form_class = AreaForm
    success_url = reverse_lazy("municipalizacion:area_list")
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
                return ["equipoMunicipal/area_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 9:
            return redirect('municipalizacion:home_equipo_municipal')
        return redirect("municipalizacion:area_list")

class AreaEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Area
    template_name = "municipalizacion/area_form.html"
    context_object_name = "obj"
    form_class = AreaForm
    success_url = reverse_lazy("municipalizacion:area_list")
    login_url = 'app:login'

class AreaDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Area
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:area_list")
