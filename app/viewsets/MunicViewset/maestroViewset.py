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
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.models import Maestro, Persona, IdiomaPersona
from app.forms import MaestroForm, PersonaForm,IdPerForm
from django.db import IntegrityError, transaction
from django.forms import formset_factory
from app.models.educacion_model.idioma import idioma

class MaesView(RolesCooMunicipalEquipoMunicipalMixin, generic.ListView):
    model = Maestro
    template_name = 'municipalizacion/maerstro_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/maerstro_list.html"]

class MaesNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = Maestro
    template_name = 'municipalizacion/maerstro_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = MaestroForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:maes_list")
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
                return ["equipoMunicipal/maerstro_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(MaesNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idiomas_maestro')
        context['errors_forms'] = {}
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Maestro, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST, prefix = 'idiomas_maestro')
        try:
            with transaction.atomic():
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    maestro= form2.save(commit=False)
                    maestro.persona_maestro = persona
                    maestro.save()
                    if len(form3.cleaned_data) == 1:
                        if form3.cleaned_data[0]:
                            for maestros_idiomas in form3:
                                idioma = maestros_idiomas.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    elif len(form3.cleaned_data) >=1:
                        for maestros_idiomas in form3:
                            if maestros_idiomas.cleaned_data:
                                idioma = maestros_idiomas.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    if self.request.user.user_profile.rol.id == 9:
                        return redirect('educacion:home_equipo_municipal')
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    print(form2.errors)
                    errors = {
                        'form':{'erros':form.errors, 'name':'Persona'},
                        'form2':{'erros':form2.errors, 'name':'ComisionNA'},
                        'form3':{'erros':form3.errors, 'name':'IdiomaPersona'},
                    }
                    print(errors)
                    return self.render_to_response(self.get_context_data(form=form,
                        form2=form2,
                        form3=form3,
                    ))
        except IntegrityError:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class MaesEdit(RolesCooMunicipalEquipoMunicipalMixin, generic.UpdateView):
    model = Maestro
    template_name = "municipalizacion/maerstro_edit.html"
    form_class = PersonaForm
    second_form_class = MaestroForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:maes_list")
    login_url = 'app:login'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/maerstro_edit.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_maestro'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        maestro = self.get_object()
        persona_maestro = maestro.persona_maestro
        idioma = IdiomaPersona.objects.filter(persona=persona_maestro)

        form = self.form_class(request.POST, request.FILES, instance = persona_maestro)
        form2 = self.second_form_class(request.POST, instance = maestro)

        with transaction.atomic():
            for idi_maestro in idioma:
                form3 = self.third_form_class(request.POST, instance = idi_maestro, prefix='idiomas_maestro')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        maestro = self.get_object()
        persona_maestro = maestro.persona_maestro

        try:
            formid_maestro = formset_factory(IdPerForm, extra=0)
            listado_idmaestro = []
            idiom_maestro = IdiomaPersona.objects.filter(persona=persona_maestro)
            for id_ma in idiom_maestro:
                listado_idmaestro.append({
                    'idioma':id_ma.idioma.id,
                    'estado_ip':id_ma.estado_ip
                })
            formset_idmaestro = formid_maestro(initial=listado_idmaestro, prefix='idiomas_maestro')
        except:
            print("Ocurrió un error")
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona_maestro)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = maestro)
        if 'form3' not in context:
            context['form3'] = formset_idmaestro
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class MaesDetail(RolesCooMunicipalEquipoMunicipalMixin, generic.DetailView):
    template_name = "municipalizacion/maestro_detail.html"
    model = Maestro

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/maestro_detail.html"]

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


class MaesDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Maestro
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:maes_list")
