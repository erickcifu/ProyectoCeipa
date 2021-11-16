from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.models import Beneficiado, Persona, IdiomaPersona, TutorMuni, Area, BeneficiadoArea
from app.forms import BenForm, PersonaForm, IdPerForm, TutorMuniForm
from django.forms import formset_factory
from django.db import IntegrityError, transaction
from app.models.educacion_model.idioma import idioma

class BenView(RolesCooMunicipalEquipoMunicipalMixin, generic.ListView):
    model = Beneficiado
    template_name = 'municipalizacion/beneficiado_list.html'
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
                return ["equipoMunicipal/beneficiado_list.html"]


class BenNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = Beneficiado
    template_name = 'municipalizacion/beneficiado_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = BenForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    four_form_class = TutorMuniForm
    success_url = reverse_lazy("municipalizacion:ben_list")
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
                return ["equipoMunicipal/beneficiado_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(BenNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idiomas')
        if 'form4' not in context:
            context['form4'] = self.four_form_class()
        context['errors_forms'] = {}
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Beneficiado, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST, prefix = 'idiomas')
        form4 = self.four_form_class(request.POST, request.FILES)

        try:
            with transaction.atomic():
                if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
                    persona = form.save()
                    beneficiado = form2.save(commit=False)
                    beneficiado.persona = persona
                    beneficiado.tutor = form4.save()
                    beneficiado.save()
                    if len(form3.cleaned_data) == 1:
                        if form3.cleaned_data[0]:
                            for form_idiomas in form3:
                                idioma = form_idiomas.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    elif len(form3.cleaned_data) >=1:
                        for form_idiomas in form3:
                            if form_idiomas.cleaned_data:
                                idioma = form_idiomas.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    if self.request.user.user_profile.rol.id == 9:
                        return redirect('educacion:home_equipo_municipal')

                    return HttpResponseRedirect(self.get_success_url())
                else:
                    print(form2.errors)
                    errors = {
                        'form':{'erros':form.errors, 'name':'Persona'},
                        'form2':{'erros':form2.errors, 'name':'Beneficiado'},
                        'form3':{'erros':form3.errors, 'name':'IdiomaPersona'},
                        'form4':{'erros':form4.errors, 'name':'TutorMuni'},
                    }
                    print(errors)
                    return self.render_to_response(self.get_context_data(form=form,
                        form2=form2,
                        form3=form3,
                        form4=form4,
                    ))
        except IntegrityError:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))

class BenEdit(RolesCooMunicipalEquipoMunicipalMixin, generic.UpdateView):
    template_name = "municipalizacion/benefEdit.html"
    success_url = reverse_lazy("municipalizacion:ben_list")
    model = Beneficiado
    form_class = PersonaForm
    second_form_class = BenForm
    third_form_class = IdPerForm
    four_form_class = TutorMuniForm


    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/benefEdit.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        beneficiado = self.get_object()
        persona = beneficiado.persona
        idioma = IdiomaPersona.objects.filter(persona=persona)
        tutor = beneficiado.tutor

        form = self.form_class(request.POST, request.FILES, instance = persona)
        form2 = self.second_form_class(request.POST, instance = beneficiado)
        form4 = self.four_form_class(request.POST, instance = tutor)

        with transaction.atomic():
            for idi in idioma:
                form3 = self.third_form_class(request.POST, instance = idi, prefix='idiomas')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid() and form4.is_valid():
                form.save()
                form2.save()
                form4.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))

    def get(self, request, *args, **kwargs):
        beneficiado = self.get_object()
        persona = beneficiado.persona
        tutor = beneficiado.tutor

        try:
            formidper = formset_factory(IdPerForm, extra=0)
            listadoIdper = []
            idiomas = IdiomaPersona.objects.filter(persona=persona)
            for i in idiomas:
                listadoIdper.append({
                    'idioma':i.idioma.id,
                    'estado_ip':i.estado_ip
                })
                print( listadoIdper)
            formsetidper = formidper(initial=listadoIdper, prefix='idiomas')
        except:
            print("error")
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = beneficiado)
        if 'form3' not in context:
            context['form3'] = formsetidper
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance = tutor)

        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class BenDetail(RolesCooMunicipalEquipoMunicipalMixin, generic.DetailView):
    template_name = "municipalizacion/ben_detail.html"
    model = Beneficiado

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/ben_detail.html"]


    def get_idioma(self, persona):
        return IdiomaPersona.objects.filter(persona=persona)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        beneficiado = self.get_object()
        persona = beneficiado.persona
        context['item'] = beneficiado
        context['tutor'] = beneficiado.tutor
        context['persona'] = persona
        context['idioma_persona'] = self.get_idioma(persona)
        return context


class BenDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Beneficiado
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:ben_list")

#Listado de participantes por area
class ListarPorArea(RolesCooMunicipalEquipoMunicipalMixin, generic.ListView):
    model = BeneficiadoArea
    template_name = "municipalizacion/listar_ben_por_area.html"
    context_object_name = 'obj'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/listar_ben_por_area.html"]

    def get_queryset(self):
        id_area = self.request.GET.get("id_area")
        if id_area:
            return Beneficiado.objects.filter(ba_benef__area_id = int(id_area))

        return Beneficiado.objects.filter(ba_benef__area_id__in=Area.objects.filter(estado_area=True).values_list('id'))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['areas'] = Area.objects.all()
        id_area = None
        try:
            id_area = Area.objects.filter(id=int(self.request.GET.get("id_area"))).first()
        except:
            id_area = None
        context['id_area'] = id_area
        return context
