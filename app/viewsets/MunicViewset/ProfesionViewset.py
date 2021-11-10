from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from app.models import Profesion
from app.forms import ProfesionForm

class ProfView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Profesion
    template_name = 'municipalizacion/profesion_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ProfNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = Profesion
    template_name = 'municipalizacion/profesion_form.html'
    context_object_name = "obj"
    form_class = ProfesionForm
    success_url = reverse_lazy("municipalizacion:prof_list")
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
                return ["equipoMunicipal/profesion_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 9:
            return redirect('municipalizacion:home_equipo_municipal')
        return redirect("municipalizacion:prof_list")

class ProfEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Profesion
    template_name = "municipalizacion/profesion_form.html"
    context_object_name = "obj"
    form_class = ProfesionForm
    success_url = reverse_lazy("municipalizacion:prof_list")
    login_url = 'app:login'

class ProfDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Profesion
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:prof_list")
