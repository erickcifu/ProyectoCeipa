from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from django.db import IntegrityError, transaction
from app.models import LiderComunitario, IdiomaPersona, Persona
from app.forms import LiderComuniMuniForm, IdPerForm, PersonaForm

class LiderComunitarioMuniView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = LiderComunitario
    template_name = 'municipalizacion/lidercomuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class LiderComunitarioNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = LiderComunitario
    template_name = 'municipalizacion/lidercomuni_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = LiderComuniMuniForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
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
                return ["equipoMunicipal/lidercomuni_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(LiderComunitarioNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(LiderComunitario, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST)

                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    lidercom = form2.save(commit=False)
                    lidercom.persona = persona
                    lidercom.save()
                    idioma = form3.save(commit=False)
                    idioma.persona = persona
                    idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
        except IntegrityError:
            handle_exception()
class LiderComunitarioEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    template_name = "municipalizacion/lidercomuni_form.html"
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
    model = LiderComunitario
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = LiderComuniMuniForm
    third_form_class = IdPerForm
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class

        return context

    def post(self, request, *args, **kwargs):
        lidercom = self.get_object()
        persona = lidercom.persona
        idioma = persona.I_persona.first()

        form = self.form_class(request.POST, instance = persona)
        form2 = self.second_form_class(request.POST, instance = lidercom)
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
        lidercom = self.get_object()
        persona = lidercom.persona
        idioma = persona.I_persona.first()

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = lidercom)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance = idioma)
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class LiderComunitarioDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = LiderComunitario
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
