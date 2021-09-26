from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import psicologico
from app.forms import PsicoForm

class PicoView(LoginRequiredMixin, generic.ListView):
    model = psicologico
    template_name = 'educacion/psico_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PsicoNew(LoginRequiredMixin, generic.CreateView):
    model = psicologico
    template_name = "educacion/psico_form.html"
    context_object_name = "obj"
    form_class = PsicoForm
    success_url = reverse_lazy("educacion:psico_list")
    login_url = 'app:login'

class PsicoEdit(LoginRequiredMixin, generic.UpdateView):
    model = psicologico
    template_name = "educacion/psico_form.html"
    context_object_name = "obj"
    form_class = PsicoForm
    success_url = reverse_lazy("educacion:psico_list")
    login_url = 'app:login'

class PsicoDel(LoginRequiredMixin, generic.DeleteView):
    model = psicologico
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:psico_list")
