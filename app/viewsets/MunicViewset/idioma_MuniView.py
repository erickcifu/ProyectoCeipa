from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import idioma
from app.forms import IdiomaMuniForm

class IdiomaMuniView(LoginRequiredMixin, generic.ListView):
    model = idioma
    template_name = 'municipalizacion/idiomaMuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class IdiomaMuniNew(LoginRequiredMixin, generic.CreateView):
    model = idioma
    template_name = 'municipalizacion/idiomaMuni_form.html'
    context_object_name = "obj"
    form_class = IdiomaMuniForm
    success_url = reverse_lazy("educacion:idiomaMuni_list")
    login_url = 'app:login'

class IdiomaMuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = idioma
    template_name = "municipalizacion/idiomaMuni_form.html"
    context_object_name = "obj"
    form_class = IdiomaMuniForm
    success_url = reverse_lazy("educacion:idiomaMuni_list")
    login_url = 'app:login'

class IdiomaMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = idioma
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:idiomaMuni_list")
