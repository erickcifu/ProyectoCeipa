from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from app.models import departamento
from app.forms import DepartamentoForm

class DepsocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = departamento
    template_name = 'socioproductivo/depsocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class DepsocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = departamento
    template_name = "socioproductivo/depsocio_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("socioproductivo:depsocio_list")
    login_url = 'app:login'

class DepsocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = departamento
    template_name = "socioproductivo/depsocio_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("socioproductivo:depsocio_list")
    login_url = 'app:login'

class DepsocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = departamento
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:depsocio_list")
