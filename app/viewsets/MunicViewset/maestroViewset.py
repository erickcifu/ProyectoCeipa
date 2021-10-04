from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Maestro
from app.forms import MaestroForm

class MaesView(LoginRequiredMixin, generic.ListView):
    model = Maestro
    template_name = 'municipalizacion/maerstro_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MaesNew(LoginRequiredMixin, generic.CreateView):
    model = Maestro
    template_name = 'municipalizacion/maerstro_form.html'
    context_object_name = "obj"
    form_class = MaestroForm
    success_url = reverse_lazy("municipalizacion:maes_list")
    login_url = 'app:login'

class MaesEdit(LoginRequiredMixin, generic.UpdateView):
    model = Maestro
    template_name = "municipalizacion/maerstro_form.html"
    context_object_name = "obj"
    form_class = MaestroForm
    success_url = reverse_lazy("municipalizacion:maes_list")
    login_url = 'app:login'

class MaesDel(LoginRequiredMixin, generic.DeleteView):
    model = Maestro
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:maes_list")
