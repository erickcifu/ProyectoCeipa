from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import GrupoNA
from app.forms import GrupoNAForm

class GrupoNAView(LoginRequiredMixin, generic.ListView):
    model = GrupoNA
    template_name = 'socioproductivo/grupona_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GrupoNANew(LoginRequiredMixin, generic.CreateView):
    model = GrupoNA
    template_name = "socioproductivo/grupona_form.html"
    context_object_name = "obj"
    form_class = GrupoNAForm
    success_url = reverse_lazy("socioproductivo:grupona_list")
    login_url = 'app:login'

class GrupoNAEdit(LoginRequiredMixin, generic.UpdateView):
    model = GrupoNA
    template_name = "socioproductivo/grupona_form.html"
    context_object_name = "obj"
    form_class = GrupoNAForm
    success_url = reverse_lazy("socioproductivo:grupona_list")
    login_url = 'app:login'

class GrupoNADel(LoginRequiredMixin, generic.DeleteView):
    model = GrupoNA
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:grupona_list")
