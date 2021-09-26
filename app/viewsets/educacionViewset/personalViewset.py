from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import personalEducativo
from app.forms import PersonalForm

class PersonalView(LoginRequiredMixin, generic.ListView):
    model = personalEducativo
    template_name = 'educacion/personal_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PersonalNew(LoginRequiredMixin, generic.CreateView):
    model = personalEducativo
    template_name = 'educacion/personal_form.html'
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("educacion:personal_list")
    login_url = 'app:login'

class PersonalEdit(LoginRequiredMixin, generic.UpdateView):
    model = personalEducativo
    template_name = "educacion/personal_form.html"
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("educacion:personal_list")
    login_url = 'app:login'

class PersonalDel(LoginRequiredMixin, generic.DeleteView):
    model = personalEducativo
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:personal_list")
