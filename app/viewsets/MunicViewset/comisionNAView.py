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
from django.db import IntegrityError, transaction
from django.forms import formset_factory

from app.models import ComisionNA, Persona, IdiomaPersona
from app.forms import Comision_NAForm, PersonaForm, IdPerForm
from app.models.educacion_model.idioma import idioma

class ComisionNAView(RolesCooMunicipalEquipoMunicipalMixin, generic.ListView):
    model = ComisionNA
    template_name = 'municipalizacion/comisionNA_list.html'
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
                return ["equipoMunicipal/comisionNA_list.html"]


class ComisionNANew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = ComisionNA
    template_name = 'municipalizacion/comisionNA_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = Comision_NAForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:comisionNA_list")
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
                return ["equipoMunicipal/comisionNA_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(ComisionNANew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idiomas_na')
        context['errors_forms'] = {}
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(ComisionNA, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST, prefix = 'idiomas_na')

        try:
            with transaction.atomic():
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    comision_na = form2.save(commit=False)
                    comision_na.persona_cna = persona
                    comision_na.save()
                    if len(form3.cleaned_data) == 1:
                        if form3.cleaned_data[0]:
                            for comision_idiomas in form3:
                                idioma = comision_idiomas.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    elif len(form3.cleaned_data) >=1:
                        for comision_idiomas in form3:
                            if comision_idiomas.cleaned_data:
                                idioma = comision_idiomas.save(commit=False)
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

class ComisionNAEdit(RolesCooMunicipalEquipoMunicipalMixin, generic.UpdateView):
    model = ComisionNA
    template_name = "municipalizacion/comisionNA_edit.html"
    form_class = PersonaForm
    second_form_class = Comision_NAForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:comisionNA_list")
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
                return ["equipoMunicipal/comisionNA_edit.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_na'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        comna = self.get_object()
        persona_cna = comna.persona_cna
        idioma = IdiomaPersona.objects.filter(persona=persona_cna)
        form = self.form_class(request.POST, instance = persona_cna)
        form2 = self.second_form_class(request.POST, instance = comna)

        with transaction.atomic():
            for idioma_comi in idioma:
                form3 = self.third_form_class(request.POST, instance=idioma_comi, prefix='idiomas')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        comna = self.get_object()
        persona_cna = comna.persona_cna

        try:
            formidiomas = formset_factory(IdPerForm, extra=0)
            list_idcomi = []
            print(list_idcomi)
            idioma_comi = IdiomaPersona.objects.filter(persona=persona_cna)
            print('Si filtra')
            for i in idioma_comi:
                list_idcomi.append({
                    'idioma': i.idioma.id,
                    'estado_ip': i.estado_ip
                })
            print('List: ', list_idcomi)
            formsetidcomi = formidiomas(initial=list_idcomi, prefix='idiomas')
        except:
            print('Ocurrió un error')
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona_cna)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = comna)
        if 'form3' not in context:
            context['form3'] = formsetidcomi
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class ComisionNADetail(RolesCooMunicipalEquipoMunicipalMixin, generic.DetailView):
    template_name = "municipalizacion/comisionNA_detail.html"
    model = ComisionNA

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/comisionNA_detail.html"]

    def get_idioma_na(self, persona_na):
        return IdiomaPersona.objects.filter(persona=persona_na)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comna = self.get_object()
        persona_na = comna.persona_cna
        context['item'] = comna
        context['persona_na'] = persona_na
        context['id_per_na'] = self.get_idioma_na(persona_na)
        return context

class ComisionNADel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = ComisionNA
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:comisionNA_list")
