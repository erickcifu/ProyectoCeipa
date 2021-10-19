from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import centro_educativo
from app.forms import CentEduForm

class CenEdView(LoginRequiredMixin, generic.ListView):
    model = centro_educativo
    template_name = 'educacion/centedu_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CenEdNew(LoginRequiredMixin, generic.CreateView):
    model = centro_educativo
    template_name = "educacion/centedu_form.html"
    context_object_name = "obj"
    form_class = CentEduForm
    success_url = reverse_lazy("educacion:centedu_list")
    login_url = 'app:login'

class CenEdEdit(LoginRequiredMixin, generic.UpdateView):
    model = centro_educativo
    template_name = "educacion/centedu_form.html"
    context_object_name = "obj"
    form_class = CentEduForm
    success_url = reverse_lazy("educacion:centedu_list")
    login_url = 'app:login'

class CenEdDel(LoginRequiredMixin, generic.DeleteView):
    model = centro_educativo
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:centedu_list")
