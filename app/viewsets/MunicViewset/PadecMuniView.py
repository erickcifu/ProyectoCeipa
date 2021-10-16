from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Padecimiento
from app.forms import PadeForm

class PadMuniView(LoginRequiredMixin, generic.ListView):
    model = Padecimiento
    template_name = 'municipalizacion/padmuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadMuniNew(LoginRequiredMixin, generic.CreateView):
    model = Padecimiento
    template_name = "municipalizacion/padmuni_form.html"
    context_object_name = "obj"
    form_class = PadeForm
    success_url = reverse_lazy("municipalizacion:padmuni_list")
    login_url = 'app:login'

class PadMuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = Padecimiento
    template_name = "municipalizacion/padmuni_form.html"
    context_object_name = "obj"
    form_class = PadeForm
    success_url = reverse_lazy("municipalizacion:padmuni_list")
    login_url = 'app:login'

class PadMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = Padecimiento
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:padmuni_list")
