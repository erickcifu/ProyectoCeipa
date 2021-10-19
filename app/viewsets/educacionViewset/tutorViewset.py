from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tutor
from app.forms import TutorForm

class TutorView(LoginRequiredMixin, generic.ListView):
    model = Tutor
    template_name = 'educacion/tutor_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TutorNew(LoginRequiredMixin, generic.CreateView):
    model = Tutor
    template_name = 'educacion/tutor_form.html'
    context_object_name = "obj"
    form_class = TutorForm
    success_url = reverse_lazy("educacion:tutor_list")
    login_url = 'app:login'

class TutorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tutor
    template_name = "educacion/tutor_form.html"
    context_object_name = "obj"
    form_class = TutorForm
    success_url = reverse_lazy("educacion:tutor_list")
    login_url = 'app:login'

class TutorDel(LoginRequiredMixin, generic.DeleteView):
    model = Tutor
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:tutor_list")