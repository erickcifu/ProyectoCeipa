from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tipo_piso
from app.forms import TpisoForm

class Tpiso_muniView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Tipo_piso
    template_name = 'municipalizacion/pisomuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class Tpiso_muniNew(IsCoordinadorMunicipalMixin, generic.CreateView):
    model = Tipo_piso
    template_name = "municipalizacion/pisomuni_form.html"
    context_object_name = "obj"
    form_class = TpisoForm
    success_url = reverse_lazy("municipalizacion:pisomuni_list")
    login_url = 'app:login'

class Tpiso_muniEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Tipo_piso
    template_name = "municipalizacion/pisomuni_form.html"
    context_object_name = "obj"
    form_class = TpisoForm
    success_url = reverse_lazy("municipalizacion:pisomuni_list")
    login_url = 'app:login'

class Tpiso_muniDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Tipo_piso
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:pisomuni_list")
