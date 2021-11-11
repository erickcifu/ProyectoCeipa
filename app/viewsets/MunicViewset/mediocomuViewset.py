from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.models import MedioComuni, Persona, IdiomaPersona
from app.forms import MedioComuniForm, PersonaForm,IdPerForm
from django.forms import formset_factory
from django.db import IntegrityError, transaction
from app.models.educacion_model.idioma import idioma


class MedioComuniView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = MedioComuni
    template_name = 'municipalizacion/mediocomu_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MedioComuniNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = MedioComuni
    template_name = 'municipalizacion/mediocomu_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = MedioComuniForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
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
                return ["equipoMunicipal/mediocomu_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(MedioComuniNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix='idioma_medioc')
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(MedioComuni, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST, request.FILES)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST, prefix='idioma_medioc')
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    medio= form2.save(commit=False)
                    medio.persona = persona
                    medio.save()
                    for idi_medioc in form3:
                        idioma = idi_medioc.save(commit=False)
                        idioma.persona = persona
                        idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
        except IntegrityError:
            handle_exception()

class MedioComuniEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = MedioComuni
    template_name = "municipalizacion/mediocomu_form.html"
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = MedioComuniForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class

        return context

    def post(self, request, *args, **kwargs):
        medio = self.get_object()
        persona = medio.persona
        idioma = persona.I_persona.first()

        form = self.form_class(request.POST, instance = persona)
        form2 = self.second_form_class(request.POST, instance = medio)
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
        medio = self.get_object()
        persona = medio.persona
        idioma = persona.I_persona.first()

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = medio)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance = idioma)
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class MedioComuniDetail(IsCoordinadorMunicipalMixin, generic.DetailView):
    template_name = "municipalizacion/mediocomu_detail.html"
    model = MedioComuni

    def get_idioma(self, persona):
        return IdiomaPersona.objects.filter(persona=persona)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medio = self.get_object()
        persona = medio.persona
        context['item'] = medio
        context['persona'] = persona
        context['idioma_persona'] = self.get_idioma(persona)
        return context


class MedioComuniDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = MedioComuni
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
