from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tipo_muro
from app.forms import ParedForm

class ParedmuniView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Tipo_muro
    template_name = 'municipalizacion/paredmuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ParedmuniNew(IsCoordinadorMunicipalMixin, generic.CreateView):
    model = Tipo_muro
    template_name = "municipalizacion/paredmuni_form.html"
    context_object_name = "obj"
    form_class = ParedForm
    success_url = reverse_lazy("municipalizacion:paredmuni_list")
    login_url = 'app:login'

class ParedmuniEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Tipo_muro
    template_name = "municipalizacion/paredmuni_form.html"
    context_object_name = "obj"
    form_class = ParedForm
    success_url = reverse_lazy("educacion:paredmuni_list")
    login_url = 'app:login'

class ParedmuniDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Tipo_muro
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:paredmuni_list")
