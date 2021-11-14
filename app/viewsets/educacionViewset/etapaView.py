from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from app.models import Etapa
from app.forms import EtapaForm

class EtapaView(LoginRequiredMixin, generic.ListView):
    model = Etapa
    template_name = 'educacion/etapa_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EtapaNew(LoginRequiredMixin, generic.CreateView):
    model = Etapa
    template_name = 'educacion/etapa_form.html'
    context_object_name = "obj"
    form_class = EtapaForm
    success_url = reverse_lazy("educacion:etapa_list")
    success_message = "Etapa creada correctamente"
    login_url = 'app:login'

class EtapaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Etapa
    template_name = "educacion/etapa_form.html"
    context_object_name = "obj"
    form_class = EtapaForm
    success_url = reverse_lazy("educacion:etapa_list")
    login_url = 'app:login'

class EtapaDel(LoginRequiredMixin, generic.DeleteView):
    model = Etapa
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:etapa_list")
