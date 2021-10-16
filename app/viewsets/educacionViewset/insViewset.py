from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Inscripcion
from app.forms import InsForm

class InsView(LoginRequiredMixin, generic.ListView):
    model = Inscripcion
    template_name = 'educacion/ins_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class InsNew(LoginRequiredMixin, generic.CreateView):
    model = Inscripcion
    template_name = "educacion/ins_form.html"
    context_object_name = "obj"
    form_class = InsForm
    success_url = reverse_lazy("educacion:ins_list")
    login_url = 'app:login'

class InsEdit(LoginRequiredMixin, generic.UpdateView):
    model = Inscripcion
    template_name = "educacion/ins_form.html"
    context_object_name = "obj"
    form_class = InsForm
    success_url = reverse_lazy("educacion:ins_list")
    login_url = 'app:login'

class InsDel(LoginRequiredMixin, generic.DeleteView):
    model = Inscripcion
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:ins_list")
