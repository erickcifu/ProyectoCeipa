from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import Categoria
from app.forms import CategoriaForm

class CatsocioView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'socioproductivo/catsocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CatsocioNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "socioproductivo/catsocio_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("socioproductivo:catsocio_list")
    login_url = 'app:login'

class CatsocioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "socioproductivo/catsocio_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("socioproductivo:catsocio_list")
    login_url = 'app:login'

class CatsocioDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:catsocio_list")
