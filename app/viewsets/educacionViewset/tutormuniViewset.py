from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import TutorMuni
from app.forms import TutorMuniForm

class TutorMuniView(LoginRequiredMixin, generic.ListView):
    model = TutorMuni
    template_name = 'educacion/tutormuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TutorMuniNew(LoginRequiredMixin, generic.CreateView):
    model = TutorMuni
    template_name = 'educacion/tutormuni_form.html'
    context_object_name = "obj"
    form_class = TutorMuniForm
    success_url = reverse_lazy("educacion:tutormuni_list")
    login_url = 'app:login'

class TutorMuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = TutorMuni
    template_name = "educacion/tutormuni_form.html"
    context_object_name = "obj"
    form_class = TutorMuniForm
    success_url = reverse_lazy("educacion:tutormuni_list")
    login_url = 'app:login'

class TutorMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = TutorMuni
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:tutormuni_list")