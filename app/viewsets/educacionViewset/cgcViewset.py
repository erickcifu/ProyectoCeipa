from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Ciclo_grado_curso
from app.forms import CGCForm

class CGCView(LoginRequiredMixin, generic.ListView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cgc_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CGCNew(LoginRequiredMixin, generic.CreateView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cgc_form.html'
    context_object_name = "obj"
    form_class = CGCForm
    success_url = reverse_lazy("educacion:cgc_list")
    login_url = 'app:login'

class CGCEdit(LoginRequiredMixin, generic.UpdateView):
    model = Ciclo_grado_curso
    template_name = "educacion/cgc_form.html"
    context_object_name = "obj"
    form_class = CGCForm
    success_url = reverse_lazy("educacion:cgc_list")
    login_url = 'app:login'

class CGCDel(LoginRequiredMixin, generic.DeleteView):
    model = Ciclo_grado_curso
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:cgc_list")
