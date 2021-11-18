from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import etnia
from app.forms import EtniaForm

class EtnsocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = etnia
    template_name = 'socioproductivo/etniasocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EtnsocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = etnia
    template_name = "socioproductivo/etniasocio_form.html"
    context_object_name = "obj"
    form_class = EtniaForm
    success_url = reverse_lazy("socioprodutivo:etniasocio_list")
    login_url = 'app:login'

class EtnsocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = etnia
    template_name = "socioproductivo/etniasocio_form.html"
    context_object_name = "obj"
    form_class = EtniaForm
    success_url = reverse_lazy("socioprodutivo:etniasocio_list")
    login_url = 'app:login'

class EtnsocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = etnia
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioprodutivo:etniasocio_list")
