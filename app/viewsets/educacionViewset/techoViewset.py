from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tipo_techo
from app.forms import TechoForm

class TechoView(LoginRequiredMixin, generic.ListView):
    model = Tipo_techo
    template_name = 'educacion/techo_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TechoNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_techo
    template_name = "educacion/techo_form.html"
    context_object_name = "obj"
    form_class = TechoForm
    success_url = reverse_lazy("educacion:techo_list")
    login_url = 'app:login'

class TechoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_techo
    template_name = "educacion/techo_form.html"
    context_object_name = "obj"
    form_class = TechoForm
    success_url = reverse_lazy("educacion:techo_list")
    login_url = 'app:login'

class TechoDel(LoginRequiredMixin, generic.DeleteView):
    model = Tipo_techo
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:techo_list")