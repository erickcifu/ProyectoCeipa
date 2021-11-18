from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import Tipo_muro
from app.forms import ParedForm

class ParedsocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = Tipo_muro
    template_name = 'socioproductivo/pared_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ParedsocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = Tipo_muro
    template_name = "socioproductivo/paredsocio_form.html"
    context_object_name = "obj"
    form_class = ParedForm
    success_url = reverse_lazy("socioproductivo:paredsocio_list")
    login_url = 'app:login'

class ParedsocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = Tipo_muro
    template_name = "socioproductivo/pared_form.html"
    context_object_name = "obj"
    form_class = ParedForm
    success_url = reverse_lazy("socioproductivo:paredsocio_list")
    login_url = 'app:login'

class ParedsocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = Tipo_muro
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:paredsocio_list")
