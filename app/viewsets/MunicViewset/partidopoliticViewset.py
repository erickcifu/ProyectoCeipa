from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from app.models import PartidoPolitic
from app.forms import PartidoPoliticForm

class PartidoPoliticView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = PartidoPolitic
    template_name = 'municipalizacion/partidopolitic_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PartidoPoliticNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = PartidoPolitic
    template_name = "municipalizacion/partidopolitic_form.html"
    context_object_name = "obj"
    form_class = PartidoPoliticForm
    success_url = reverse_lazy("municipalizacion:partidopolitic_list")
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
                return ["equipoMunicipal/partidopolitic_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 9:
            return redirect('municipalizacion:home_equipo_municipal')
        return redirect("municipalizacion:partidopolitic_list")

class PartidoPoliticEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = PartidoPolitic
    template_name = "municipalizacion/partidopolitic_form.html"
    context_object_name = "obj"
    form_class = PartidoPoliticForm
    success_url = reverse_lazy("municipalizacion:partidopolitic_list")
    login_url = 'app:login'

class PartidoPoliticDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = PartidoPolitic
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:partidopolitic_list")
