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
from django.forms import formset_factory
from app.models.educacion_model.idioma import idioma

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
    third_form_class = formset_factory(IdPerForm, extra=1)
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
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idioma_lider')
        context['errors_forms'] = {}
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(LiderComunitario, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST, prefix = 'idioma_lider')
        try:
            with transaction.atomic():
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    lidercom = form2.save(commit=False)
                    lidercom.persona = persona
                    lidercom.save()
                    if len(form3.cleaned_data) == 1:
                        if form3.cleaned_data[0]:
                            for idiom_lider in form3:
                                idioma = idiom_lider.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    elif len(form3.cleaned_data) >= 1:
                        for idiom_lider in form3:
                            if idiom_lider.cleaned_data:
                                idioma = idiom_lider.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    print(form2.errors)
                    errors = {
                        'form':{'erros':form.errors, 'name':'Persona'},
                        'form2':{'erros':form2.errors, 'name':'LiderComunitario'},
                        'form3':{'erros':form3.errors, 'name':'IdiomaPersona'},
                    }
                    print(errors)
                    return self.render_to_response(self.get_context_data(form=form,
                        form2=form2,
                        form3=form3,
                    ))
        except IntegrityError:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

class LiderComunitarioEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    template_name = "municipalizacion/lidercomuni_edit.html"
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
        idioma = IdiomaPersona.objects.filter(persona=persona)

        form = self.form_class(request.POST, request.FILES, instance = persona)
        form2 = self.second_form_class(request.POST, instance = lidercom)

        with transaction.atomic():
            for idi_lider in idioma:
                form3 = self.third_form_class(request.POST, instance=idi_lider, prefix='idioma_lider')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        lidercom = self.get_object()
        persona = lidercom.persona
        idioma = persona.I_persona.first()

        try:
            formidioma = formset_factory(IdPerForm, extra=0)
            listdo_idiomasl = []
            idiomas_lider = IdiomaPersona.objects.filter(persona=persona)
            for idio_lider in idiomas_lider:
                listdo_idiomasl.append({
                    'idioma': idio_lider.idioma.id,
                    'estado_ip': idio_lider.estado_ip
                })
            formset_idiomasl = formidioma(initial=listdo_idiomasl, prefix='idioma_lider')
        except:
            print('Ocurrió un error')
            return HttpResponseRedirect(self.success_url)

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = lidercom)
        if 'form3' not in context:
            context['form3'] = formset_idiomasl

        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class LiderComunitarioDetail(LoginRequiredMixin, generic.DetailView):
    template_name = "municipalizacion/lidercomuni_detail.html"
    model = LiderComunitario

    def get_idioma_lider(self, persona_lider):
        return IdiomaPersona.objects.filter(persona=persona_lider)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lidercom = self.get_object()
        persona_lider = lidercom.persona
        context['item'] = lidercom
        context['persona_lider'] = persona_lider
        context['idioma_lider'] = self.get_idioma_lider(persona_lider)
        return context

class MaesDetail(LoginRequiredMixin, generic.DetailView):
    template_name = "municipalizacion/maestro_detail.html"
    model = LiderComunitario

    def get_idioma(self, persona_maestro):
        return IdiomaPersona.objects.filter(persona=persona_maestro)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maestro = self.get_object()
        persona_maestro = maestro.persona_maestro
        context['item'] = maestro
        context['persona_maestro'] = persona_maestro
        context['idioma_maestro'] = self.get_idioma(persona_maestro)
        return context


class LiderComunitarioDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = LiderComunitario
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
