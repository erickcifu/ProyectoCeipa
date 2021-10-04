from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Beneficiado
from app.forms import BenForm

class BenView(LoginRequiredMixin, generic.ListView):
    model = Beneficiado
    template_name = 'municipalizacion/beneficiado_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class BenNew(LoginRequiredMixin, generic.CreateView):
    model = Beneficiado
    template_name = 'municipalizacion/beneficiado_form.html'
    context_object_name = "obj"
    form_class = BenForm
    success_url = reverse_lazy("municipalizacion:ben_list")
    login_url = 'app:login'

class BenEdit(LoginRequiredMixin, generic.UpdateView):
    model = Beneficiado
    template_name = "municipalizacion/beneficiado_form.html"
    context_object_name = "obj"
    form_class = BenForm
    success_url = reverse_lazy("municipalizacion:ben_list")
    login_url = 'app:login'

class BenDel(LoginRequiredMixin, generic.DeleteView):
    model = Beneficiado
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:ben_list")
