from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import PartidoPolitic
from app.forms import PartidoPoliticForm

class PartidoPoliticView(LoginRequiredMixin, generic.ListView):
    model = PartidoPolitic
    template_name = 'educacion/partidopolitic_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PartidoPoliticNew(LoginRequiredMixin, generic.CreateView):
    model = PartidoPolitic
    template_name = "educacion/partidopolitic_form.html"
    context_object_name = "obj"
    form_class = PartidoPoliticForm
    success_url = reverse_lazy("educacion:partidopolitic_list")
    login_url = 'app:login'

class PartidoPoliticEdit(LoginRequiredMixin, generic.UpdateView):
    model = PartidoPolitic
    template_name = "educacion/partidopolitic_form.html"
    context_object_name = "obj"
    form_class = PartidoPoliticForm
    success_url = reverse_lazy("educacion:partidopolitic_list")
    login_url = 'app:login'

class PartidoPoliticDel(LoginRequiredMixin, generic.DeleteView):
    model = PartidoPolitic
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:partidopolitic_list")