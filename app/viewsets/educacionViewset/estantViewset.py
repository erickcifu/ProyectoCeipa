from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import EstudiosAnt
from app.forms import EstAntForm

class EstAntView(LoginRequiredMixin, generic.ListView):
    model = EstudiosAnt
    template_name = 'educacion/estant_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EstAntNew(LoginRequiredMixin, generic.CreateView):
    model = EstudiosAnt
    template_name = "educacion/estant_form.html"
    context_object_name = "obj"
    form_class = EstAntForm
    success_url = reverse_lazy("educacion:estant_list")
    login_url = 'app:login'

class EstAntEdit(LoginRequiredMixin, generic.UpdateView):
    model = EstudiosAnt
    template_name = "educacion/estant_form.html"
    context_object_name = "obj"
    form_class = EstAntForm
    success_url = reverse_lazy("educacion:estant_list")
    login_url = 'app:login'

class EstAntDel(LoginRequiredMixin, generic.DeleteView):
    model = EstudiosAnt
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:estant_list")
