from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tipo_medio
from app.forms import TmedioForm

class TmedioView(LoginRequiredMixin, generic.ListView):
    model = Tipo_medio
    template_name = 'municipalizacion/tmedio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TmedioNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_medio
    template_name = 'municipalizacion/tmedio_form.html'
    context_object_name = "obj"
    form_class = TmedioForm
    success_url = reverse_lazy("municipalizacion:tmedio_list")
    login_url = 'app:login'

class TmedioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_medio
    template_name = "municipalizacion/tmedio_form.html"
    context_object_name = "obj"
    form_class = TmedioForm
    success_url = reverse_lazy("municipalizacion:tmedio_list")
    login_url = 'app:login'

class TmedioDel(LoginRequiredMixin, generic.DeleteView):
    model = Tipo_medio
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:tmedio_list")
