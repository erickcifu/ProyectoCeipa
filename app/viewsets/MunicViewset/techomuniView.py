from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tipo_techo
from app.forms import TechoForm

class TechomuniView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Tipo_techo
    template_name = 'municipalizacion/techomuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TechomuniNew(IsCoordinadorMunicipalMixin, generic.CreateView):
    model = Tipo_techo
    template_name = "municipalizacion/techomuni_form.html"
    context_object_name = "obj"
    form_class = TechoForm
    success_url = reverse_lazy("municipalizacion:techomuni_list")
    login_url = 'app:login'

class TechomuniEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Tipo_techo
    template_name = "municipalizacion/techomuni_form.html"
    context_object_name = "obj"
    form_class = TechoForm
    success_url = reverse_lazy("municipalizacion:techomuni_list")
    login_url = 'app:login'

class TechomuniDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Tipo_techo
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:techomuni_list")
