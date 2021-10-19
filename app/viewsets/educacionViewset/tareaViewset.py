from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import tarea
from app.forms import TareaForm

class TareaView(LoginRequiredMixin, generic.ListView):
    model = tarea
    template_name = 'educacion/tarea_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TareaNew(LoginRequiredMixin, generic.CreateView):
    model = tarea
    template_name = 'educacion/tarea_form.html'
    context_object_name = "obj"
    form_class = TareaForm
    success_url = reverse_lazy("educacion:tarea_list")
    login_url = 'app:login'

class TareaEdit(LoginRequiredMixin, generic.UpdateView):
    model = tarea
    template_name = "educacion/tarea_form.html"
    context_object_name = "obj"
    form_class = TareaForm
    success_url = reverse_lazy("educacion:tarea_list")
    login_url = 'app:login'

class TareaDel(LoginRequiredMixin, generic.DeleteView):
    model = tarea
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:tarea_list")
