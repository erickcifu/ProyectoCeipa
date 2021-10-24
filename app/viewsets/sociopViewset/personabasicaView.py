from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import PersonaBasica
from app.forms import PersonaBForm

class PersonaBasicaView(LoginRequiredMixin, generic.ListView):
    model = PersonaBasica
    template_name = 'socioproductivo/personabasica_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PersonaBasicaNew(LoginRequiredMixin, generic.CreateView):
    model = PersonaBasica
    template_name = "socioproductivo/personabasica_form.html"
    context_object_name = "obj"
    form_class = PersonaBForm
    success_url = reverse_lazy("socioproductivo:personabasica_list")
    login_url = 'app:login'

class PersonaBasicaEdit(LoginRequiredMixin, generic.UpdateView):
    model = PersonaBasica
    template_name = "socioproductivo/personabasica_form.html"
    context_object_name = "obj"
    form_class = PersonaBForm
    success_url = reverse_lazy("socioproductivo:personabasica_list")
    login_url = 'app:login'

class PersonaBasicaDel(LoginRequiredMixin, generic.DeleteView):
    model = PersonaBasica
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:personabasica_list")
