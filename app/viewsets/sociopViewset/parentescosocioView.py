from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import Parentesco
from app.forms import ParentescoForm

class ParentescosocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = Parentesco
    template_name = 'socioproductivo/parensocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ParentescosocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = Parentesco
    template_name = "socioproductivo/parensocio_form.html"
    context_object_name = "obj"
    form_class = ParentescoForm
    success_url = reverse_lazy("socioproductivo:parensocio_list")
    login_url = 'app:login'

class ParentescosocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = Parentesco
    template_name = "socioproductivo/parensocio_form.html"
    context_object_name = "obj"
    form_class = ParentescoForm
    success_url = reverse_lazy("socioproductivo:parensocio_list")
    login_url = 'app:login'

class ParentescosocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = Parentesco
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:parensociolist")
