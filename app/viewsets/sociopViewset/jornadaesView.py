from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import JornadaEstudios
from app.forms import JornadaesForm

class JornadaEsView(LoginRequiredMixin, generic.ListView):
    model = JornadaEstudios
    template_name = 'socioproductivo/jornadaes_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class JornadaEsNew(LoginRequiredMixin, generic.CreateView):
    model = JornadaEstudios
    template_name = "socioproductivo/jornadaes_form.html"
    context_object_name = "obj"
    form_class = JornadaesForm
    success_url = reverse_lazy("socioproductivo:jornadaes_list")
    login_url = 'app:login'

class JornadaEsEdit(LoginRequiredMixin, generic.UpdateView):
    model = JornadaEstudios
    template_name = "socioproductivo/jornadaes_form.html"
    context_object_name = "obj"
    form_class = JornadaesForm
    success_url = reverse_lazy("socioproductivo:jornadaes_list")
    login_url = 'app:login'

class JornadaEsDel(LoginRequiredMixin, generic.DeleteView):
    model = JornadaEstudios
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:jornadaes_list")
