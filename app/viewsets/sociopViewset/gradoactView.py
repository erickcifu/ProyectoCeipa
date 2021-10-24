from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Grado_actual
from app.forms import GradoactForm

class GradoactView(LoginRequiredMixin, generic.ListView):
    model = Grado_actual
    template_name = 'socioproductivo/gradoact_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GradoactNew(LoginRequiredMixin, generic.CreateView):
    model = Grado_actual
    template_name = "socioproductivo/gradoact_form.html"
    context_object_name = "obj"
    form_class = GradoactForm
    success_url = reverse_lazy("socioproductivo:gradoact_list")
    login_url = 'app:login'

class GradoactEdit(LoginRequiredMixin, generic.UpdateView):
    model = Grado_actual
    template_name = "socioproductivo/gradoact_form.html"
    context_object_name = "obj"
    form_class = GradoactForm
    success_url = reverse_lazy("socioproductivo:gradoact_list")
    login_url = 'app:login'

class GradoactDel(LoginRequiredMixin, generic.DeleteView):
    model = Grado_actual
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:gradoact_list")
