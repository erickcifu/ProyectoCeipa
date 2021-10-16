from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import LiderComunitario
from app.forms import LiderComuniMuniForm

class LiderComunitarioMuniView(LoginRequiredMixin, generic.ListView):
    model = LiderComunitario
    template_name = 'municipalizacion/lidercomuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class LiderComunitarioNew(LoginRequiredMixin, generic.CreateView):
    model = LiderComunitario
    template_name = 'municipalizacion/lidercomuni_form.html'
    context_object_name = "obj"
    form_class = LiderComuniMuniForm
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
    login_url = 'app:login'

class LiderComunitarioEdit(LoginRequiredMixin, generic.UpdateView):
    model = LiderComunitario
    template_name = "municipalizacion/lidercomuni_form.html"
    context_object_name = "obj"
    form_class = LiderComuniMuniForm
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
    login_url = 'app:login'

class LiderComunitarioDel(LoginRequiredMixin, generic.DeleteView):
    model = LiderComunitario
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")