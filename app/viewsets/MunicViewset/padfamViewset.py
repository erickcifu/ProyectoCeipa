from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import PadresFamilia
from app.forms import PadFamForm

class PadFamView(LoginRequiredMixin, generic.ListView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadFamNew(LoginRequiredMixin, generic.CreateView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_form.html'
    context_object_name = "obj"
    form_class = PadFamForm
    success_url = reverse_lazy("municipalizacion:padfam_list")
    login_url = 'app:login'

class PadFamEdit(LoginRequiredMixin, generic.UpdateView):
    model = PadresFamilia
    template_name = "municipalizacion/padfam_form.html"
    context_object_name = "obj"
    form_class = PadFamForm
    success_url = reverse_lazy("municipalizacion:padfam_list")
    login_url = 'app:login'

class PadFamDel(LoginRequiredMixin, generic.DeleteView):
    model = PadresFamilia
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:padfam_list")
