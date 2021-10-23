from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import OcupacionTutor
from app.forms import OcupTutorForm

class OcupTutorView(LoginRequiredMixin, generic.ListView):
    model = OcupacionTutor
    template_name = 'socioproductivo/ocupTutor_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class OcupTutorNew(LoginRequiredMixin, generic.CreateView):
    model = OcupacionTutor
    template_name = "socioproductivo/ocupTutor_form.html"
    context_object_name = "obj"
    form_class = OcupTutorForm
    success_url = reverse_lazy("socioproductivo:ocupTutor_list")
    login_url = 'app:login'

class OcupTutorEdit(LoginRequiredMixin, generic.UpdateView):
    model = OcupacionTutor
    template_name = "socioproductivo/ocupTutor_form.html"
    context_object_name = "obj"
    form_class = OcupTutorForm
    success_url = reverse_lazy("socioproductivo:ocupTutor_list")
    login_url = 'app:login'

class OcupTutorDel(LoginRequiredMixin, generic.DeleteView):
    model = OcupacionTutor
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:ocupTutor_list")
