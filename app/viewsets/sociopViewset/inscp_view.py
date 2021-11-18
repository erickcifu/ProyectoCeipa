from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import Inscripcionp, PersonaBasica, Taller
from app.forms import InscpForm, InscTallerForm

class InscpView(LoginRequiredMixin, generic.ListView):
    model = Inscripcionp
    template_name = 'socioproductivo/inscp_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class InscpNew(LoginRequiredMixin, generic.CreateView):
    model = Inscripcionp
    template_name = "socioproductivo/inscp_form.html"
    context_object_name = "obj"
    form_class = InscpForm
    success_url = reverse_lazy("socioproductivo:inscp_list")
    login_url = 'app:login'

class InscpEdit(LoginRequiredMixin, generic.UpdateView):
    model = Inscripcionp
    template_name = "socioproductivo/inscp_form.html"
    context_object_name = "obj"
    form_class = InscpForm
    success_url = reverse_lazy("socioproductivo:inscp_list")
    login_url = 'app:login'

class InscpDel(LoginRequiredMixin, generic.DeleteView):
    model = Inscripcionp
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:inscp_list")

class InscribirParticipanteTaller(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = Inscripcionp
    template_name = "socioproductivo/inscp_participante.html"
    context_object_name = "obj"
    form_class = InscTallerForm
    success_url = reverse_lazy("socioproductivo:part_taller")
    login_url = 'app:login'
    id_taller = ''

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 10 or user == 11:
                return [self.template_name]
            elif user == 12:
                return ["equipoSocioproductivo/Emprendimiento_form.html"]
            else:
                return [self.template_name]

    def get_queryset(self):
        return Taller.objects.all()

    def get_object(self):
        id_taller = self.kwargs.get('pk')
        qs = None
        if id_taller:
            qs = self.get_queryset().filter(id=id_taller).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_taller'] = self.get_object().id if self.get_object() else ''
        context['talleres'] = Taller.objects.all()
        #context['participantes'] = PersonaBasica.objects.exclude(ins_per__taller__id = self.get_object().id)
        return context

    def form_valid(self,form):
        if form.is_valid():
            self.id_taller = self.get_object()
            if self.id_taller:
                inscp = Inscripcionp(**form.cleaned_data, taller=self.id_taller)
                inscp.save()
                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
