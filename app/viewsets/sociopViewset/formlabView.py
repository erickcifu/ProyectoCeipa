from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import FormacionLab, PersonaBasica
from app.forms import LaboralSocioForm, LaboralEditForm


class FormLabView(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.ListView):
    model = FormacionLab
    template_name = 'socioproductivo/listar_formacion.html'
    context_object_name = 'obj'
    login_url = 'app:login'


class FormLabNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = FormacionLab
    template_name = "socioproductivo/formlab_form.html"
    context_object_name = "obj"
    form_class = LaboralSocioForm
    success_url = reverse_lazy("socioproductivo:part_formlab")
    login_url = 'app:login'
    id_participante = ''

    def get_queryset(self):
        return PersonaBasica.objects.all()

    def get_object(self):
        participante_id = self.kwargs.get('pk')
        qs = None
        if participante_id:
            qs = self.get_queryset().filter(id=participante_id).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_participante'] = self.get_object().id if self.get_object() else ''
        context['participantes'] = PersonaBasica.objects.all()
        return context
    '''
    def post(self, request, *args, **kwargs):
        self.id_participante = self.get_object()
        super().post(request, *args, **kwargs)
    '''

    def form_valid(self, form):
        if form.is_valid():
            self.id_participante = self.get_object()
            if self.id_participante:
                formlab_persona = FormacionLab(**form.cleaned_data, persona_formacion=self.id_participante)
                formlab_persona.save()
                print('se guardó', formlab_persona)
                return redirect("socioproductivo:part_formlab")
            else:
                return self.render_to_response(self.get_context_data(form=form))

class formlabEdit(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.UpdateView):
    model = FormacionLab
    template_name = "socioproductivo/labedit_form.html"
    context_object_name = "obj"
    form_class = LaboralEditForm
    success_url = reverse_lazy("socioproductivo:formlab_list")
    login_url = 'app:login'


class formlabDelete(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.DeleteView):
    model = FormacionLab
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:part_formlab")
    login_url = 'app:login'
