from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin
from django.contrib.messages.views import SuccessMessageMixin

from app.models import Ciclo
from app.forms import CicloForm

class CicloView(IsCoordinadorEducacionMixin, generic.ListView):
    model = Ciclo
    template_name = 'educacion/ciclo_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CicloNew(IsCoordinadorEducacionMixin, generic.CreateView):
    model = Ciclo
    template_name = 'educacion/ciclo_form.html'
    context_object_name = "obj"
    form_class = CicloForm
    success_url = reverse_lazy("educacion:ciclo_list")
    success_message = "Ciclo creado correctamente"
    login_url = 'app:login'

class CicloEdit(IsCoordinadorEducacionMixin, generic.UpdateView):
    model = Ciclo
    template_name = "educacion/ciclo_form.html"
    context_object_name = "obj"
    form_class = CicloForm
    success_url = reverse_lazy("educacion:ciclo_list")
    login_url = 'app:login'

class CicloDel(IsCoordinadorEducacionMixin, generic.DeleteView):
    model = Ciclo
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:ciclo_list")
