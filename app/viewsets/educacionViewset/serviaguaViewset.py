from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Servicio_Agua
from app.forms import ServiaguaForm

class ServiaguaView(LoginRequiredMixin, generic.ListView):
    model = Servicio_Agua
    template_name = 'educacion/serviagua_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ServiaguaNew(LoginRequiredMixin, generic.CreateView):
    model = Servicio_Agua
    template_name = "educacion/serviagua_form.html"
    context_object_name = "obj"
    form_class = ServiaguaForm
    success_url = reverse_lazy("educacion:serviagua_list")
    login_url = 'app:login'

class ServiaguaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Servicio_Agua
    template_name = "educacion/serviagua_form.html"
    context_object_name = "obj"
    form_class = ServiaguaForm
    success_url = reverse_lazy("educacion:serviagua_list")
    login_url = 'app:login'

class ServiaguaDel(LoginRequiredMixin, generic.DeleteView):
    model = Servicio_Agua
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:serviagua_list")