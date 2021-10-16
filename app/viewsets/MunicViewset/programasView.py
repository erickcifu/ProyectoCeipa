from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import ProgramaC
from app.forms import ProgramaCForm

class ProgramasView(LoginRequiredMixin, generic.ListView):
    model = ProgramaC
    template_name = 'municipalizacion/programas_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ProgramasNew(LoginRequiredMixin, generic.CreateView):
    model = ProgramaC
    template_name = "municipalizacion/programas_form.html"
    context_object_name = "obj"
    form_class = ProgramaCForm
    success_url = reverse_lazy("municipalizacion:programas_list")
    login_url = 'app:login'

class ProgramasEdit(LoginRequiredMixin, generic.UpdateView):
    model = ProgramaC
    template_name = "municipalizacion/programas_form.html"
    context_object_name = "obj"
    form_class = ProgramaCForm
    success_url = reverse_lazy("municipalizacion:programas_list")
    login_url = 'app:login'

class ProgramasDel(LoginRequiredMixin, generic.DeleteView):
    model = ProgramaC
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:programas_list")
