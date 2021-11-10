from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from app.models import PadPer
from app.forms import PadPerForm

class PadPerView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = PadPer
    template_name = 'municipalizacion/padper_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadPerNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = PadPer
    template_name = 'municipalizacion/padper_form.html'
    context_object_name = "obj"
    form_class = PadPerForm
    success_url = reverse_lazy("municipalizacion:padper_list")
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 7 or user == 8:
                return [self.template_name]
            elif user == 9:
                return ["equipoMunicipal/padper_form.html"]
            else:
                return [self.template_name]

class PadPerEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = PadPer
    template_name = "municipalizacion/padper_form.html"
    context_object_name = "obj"
    form_class = PadPerForm
    success_url = reverse_lazy("municipalizacion:padper_list")
    login_url = 'app:login'

class PadPerDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = PadPer
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:padper_list")
