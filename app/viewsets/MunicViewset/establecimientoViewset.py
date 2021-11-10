from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from app.models import Establecimiento
from app.forms import EstablecimientoForm

class EstablecimientoView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Establecimiento
    template_name = 'municipalizacion/establecimiento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EstablecimientoNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = Establecimiento
    template_name = "municipalizacion/establecimiento_form.html"
    context_object_name = "obj"
    form_class = EstablecimientoForm
    success_url = reverse_lazy("municipalizacion:establecimiento_list")
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
                return ["equipoMunicipal/establecimiento_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 9:
            return redirect('municipalizacion:home_equipo_municipal')
        return redirect("municipalizacion:establecimiento_list")

class EstablecimientoEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Establecimiento
    template_name = "municipalizacion/establecimiento_form.html"
    context_object_name = "obj"
    form_class = EstablecimientoForm
    success_url = reverse_lazy("municipalizacion:establecimiento_list")
    login_url = 'app:login'

class EstablecimientoDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Establecimiento
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:establecimiento_list")
