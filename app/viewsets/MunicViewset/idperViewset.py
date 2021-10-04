from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import IdiomaPersona
from app.forms import IdPerForm

class IdPerView(LoginRequiredMixin, generic.ListView):
    model = IdiomaPersona
    template_name = 'municipalizacion/idper_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class IdPerNew(LoginRequiredMixin, generic.CreateView):
    model = IdiomaPersona
    template_name = 'municipalizacion/idper_form.html'
    context_object_name = "obj"
    form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:idper_list")
    login_url = 'app:login'

class IdPerEdit(LoginRequiredMixin, generic.UpdateView):
    model = IdiomaPersona
    template_name = "municipalizacion/idper_form.html"
    context_object_name = "obj"
    form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:idper_list")
    login_url = 'app:login'

class IdPerDel(LoginRequiredMixin, generic.DeleteView):
    model = IdiomaPersona
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:idper_list")
