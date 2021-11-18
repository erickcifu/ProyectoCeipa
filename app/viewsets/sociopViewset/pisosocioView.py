from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import Tipo_piso
from app.forms import TpisoForm

class TpisosocioView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = Tipo_piso
    template_name = 'socioproductivo/tpisosocio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TpisosocioNew(IsCoordinadorSocioProductivoMixin, generic.CreateView):
    model = Tipo_piso
    template_name = "socioproductivo/tpisosocio_form.html"
    context_object_name = "obj"
    form_class = TpisoForm
    success_url = reverse_lazy("socioproductivo:tpisosocio_list")
    login_url = 'app:login'

class TpisosocioEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = Tipo_piso
    template_name = "socioproductivo/tpisosocio_form.html"
    context_object_name = "obj"
    form_class = TpisoForm
    success_url = reverse_lazy("socioproductivo:tpisosocio_list")
    login_url = 'app:login'

class TpisosocioDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = Tipo_piso
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:tpisosocio_list")
