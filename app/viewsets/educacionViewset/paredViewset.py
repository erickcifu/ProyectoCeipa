from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tipo_muro
from app.forms import ParedForm

class ParedView(LoginRequiredMixin, generic.ListView):
    model = Tipo_muro
    template_name = 'educacion/pared_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ParedNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_muro
    template_name = "educacion/pared_form.html"
    context_object_name = "obj"
    form_class = ParedForm
    success_url = reverse_lazy("educacion:pared_list")
    login_url = 'app:login'

class ParedEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_muro
    template_name = "educacion/pared_form.html"
    context_object_name = "obj"
    form_class = ParedForm
    success_url = reverse_lazy("educacion:pared_list")
    login_url = 'app:login'

class ParedDel(LoginRequiredMixin, generic.DeleteView):
    model = Tipo_muro
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:pared_list")