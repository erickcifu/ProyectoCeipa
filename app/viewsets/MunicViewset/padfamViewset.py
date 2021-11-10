from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from django.shortcuts import redirect
from django.db import IntegrityError, transaction

from app.models import PadresFamilia, IdiomaPersona, Persona
from app.forms import PadFamForm, IdPerForm, PersonaForm

class PadFamView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadFamNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = PadFamForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:padfam_list")
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
                return ["equipoMunicipal/padfam_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(PadFamNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(PadresFamilia, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        with transaction.atomic():
            self.object = self.get_object
            form = self.form_class(request.POST)
            form2 = self.second_form_class(request.POST)
            form3 = self.third_form_class(request.POST)

            if form.is_valid() and form2.is_valid() and form3.is_valid():
                persona = form.save()
                padfam = form2.save(commit=False)
                padfam.persona = persona
                padfam.save()
                idioma = form3.save(commit=False)
                idioma.persona = persona
                idioma.save()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class PadFamEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    template_name = "municipalizacion/padfam_form.html"
    success_url = reverse_lazy("municipalizacion:padfam_list")
    model = PadresFamilia
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = PadFamForm
    third_form_class = IdPerForm
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class

        return context

    def post(self, request, *args, **kwargs):
        padfam = self.get_object()
        persona = padfam.persona
        idioma = persona.I_persona.first()

        form = self.form_class(request.POST, instance = persona)
        form2 = self.second_form_class(request.POST, instance = padfam)
        form3 = self.third_form_class(request.POST, instance = idioma )

        with transaction.atomic():
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                form.save()
                form2.save()
                form3.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        padfam = self.get_object()
        persona = padfam.persona
        idioma = persona.I_persona.first()

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = padfam)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance = idioma)
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class PadFamDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = PadresFamilia
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:padfam_list")
