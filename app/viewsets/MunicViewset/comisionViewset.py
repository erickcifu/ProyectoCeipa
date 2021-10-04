from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Comision
from app.forms import ComisionForm

class ComView(LoginRequiredMixin, generic.ListView):
    model = Comision
    template_name = 'municipalizacion/comision_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ComNew(LoginRequiredMixin, generic.CreateView):
    model = Comision
    template_name = 'municipalizacion/comision_form.html'
    context_object_name = "obj"
    form_class = ComisionForm
    success_url = reverse_lazy("municipalizacion:com_list")
    login_url = 'app:login'

class ComEdit(LoginRequiredMixin, generic.UpdateView):
    model = Comision
    template_name = "municipalizacion/comision_form.html"
    context_object_name = "obj"
    form_class = ComisionForm
    success_url = reverse_lazy("municipalizacion:com_list")
    login_url = 'app:login'

class ComDel(LoginRequiredMixin, generic.DeleteView):
    model = Comision
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:com_list")
