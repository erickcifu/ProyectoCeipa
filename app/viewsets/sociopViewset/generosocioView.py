from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import genero
from app.forms import GeneroForm

class GenerosocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = genero
    template_name = 'socioproductivo/generosocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GenerosocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = genero
    template_name = 'socioproductivo/generosocio_form.html'
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("socioproductivo:generosocio_list")
    login_url = 'app:login'

class GenerosocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = genero
    template_name = "socioproductivo/generosocio_form.html"
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("socioproductivo:generosocio_list")
    login_url = 'app:login'

class GenerosocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = genero
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:generosocio_list")
