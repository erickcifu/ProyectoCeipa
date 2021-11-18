from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import Tipo_techo
from app.forms import TechoForm

class TechosocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = Tipo_techo
    template_name = 'socioproductivo/techosocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TechosocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = Tipo_techo
    template_name = "socioproductivo/techosocio_form.html"
    context_object_name = "obj"
    form_class = TechoForm
    success_url = reverse_lazy("socioproductivo:techosocio_list")
    login_url = 'app:login'

class TechosocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = Tipo_techo
    template_name = "socioproductivo/techosocio_form.html"
    context_object_name = "obj"
    form_class = TechoForm
    success_url = reverse_lazy("socioproductivo:techosocio_list")
    login_url = 'app:login'

class TechosocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = Tipo_techo
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:techosocio_list")
