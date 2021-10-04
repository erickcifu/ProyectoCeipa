from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Profesion
from app.forms import ProfesionForm

class ProfView(LoginRequiredMixin, generic.ListView):
    model = Profesion
    template_name = 'municipalizacion/profesion_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ProfNew(LoginRequiredMixin, generic.CreateView):
    model = Profesion
    template_name = 'municipalizacion/profesion_form.html'
    context_object_name = "obj"
    form_class = ProfesionForm
    success_url = reverse_lazy("municipalizacion:prof_list")
    login_url = 'app:login'

class ProfEdit(LoginRequiredMixin, generic.UpdateView):
    model = Profesion
    template_name = "municipalizacion/profesion_form.html"
    context_object_name = "obj"
    form_class = ProfesionForm
    success_url = reverse_lazy("municipalizacion:prof_list")
    login_url = 'app:login'

class ProfDel(LoginRequiredMixin, generic.DeleteView):
    model = Profesion
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:prof_list")
