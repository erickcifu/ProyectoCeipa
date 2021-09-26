from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import religion
from app.forms import ReligionForm

class ReligionView(LoginRequiredMixin, generic.ListView):
    model = religion
    template_name = 'educacion/religion_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ReligionNew(LoginRequiredMixin, generic.CreateView):
    model = religion
    template_name = 'educacion/religion_form.html'
    context_object_name = "obj"
    form_class = ReligionForm
    success_url = reverse_lazy("educacion:religion_list")
    login_url = 'app:login'

class ReligionEdit(LoginRequiredMixin, generic.UpdateView):
    model = religion
    template_name = "educacion/religion_form.html"
    context_object_name = "obj"
    form_class = ReligionForm
    success_url = reverse_lazy("educacion:religion_list")
    login_url = 'app:login'

class ReligionDel(LoginRequiredMixin, generic.DeleteView):
    model = religion
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:religion_list")
