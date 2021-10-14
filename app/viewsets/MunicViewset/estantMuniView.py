from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import EstudiosAnt
from app.forms import EstAntForm

class EstMuniView(LoginRequiredMixin, generic.ListView):
    model = EstudiosAnt
    template_name = 'municipalizacion/estmuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EstMuniNew(LoginRequiredMixin, generic.CreateView):
    model = EstudiosAnt
    template_name = "municipalizacion/estmuni_form.html"
    context_object_name = "obj"
    form_class = EstAntForm
    success_url = reverse_lazy("municipalizacion:estmuni_list")
    login_url = 'app:login'

class EstMuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = EstudiosAnt
    template_name = "municipalizacion/estmuni_form.html"
    context_object_name = "obj"
    form_class = EstAntForm
    success_url = reverse_lazy("municipalizacion:eestmuni_list")
    login_url = 'app:login'

class EstMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = EstudiosAnt
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:estmuni_list")
