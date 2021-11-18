from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from app.models import municipio
from app.forms import MunicipioForm

class MunicSocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = municipio
    template_name = 'socioproductivo/munisocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MunicSocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = municipio
    template_name = "socioproductivo/munisocio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("socioproductivo:municp_list")
    login_url = 'app:login'

class MunicSocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = municipio
    template_name = "socioproductivo/munisocio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("socioproductivo:municp_list")
    login_url = 'app:login'

class MunicSocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = municipio
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:municp_list")
