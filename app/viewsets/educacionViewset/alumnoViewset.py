from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from app.models.educacion_model.ciclo_grado_curso import Ciclo_grado_curso
from app.viewsets.users.maestro.mixin import IsMaestroMixin
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.mixins.CoordinadorGeneralYDirectorCentroMixin import RolesCoordinadorEducacionYDirectorCentroMixin
from app.viewsets.users.mixins.CooEducacionDirectorCentroMaestro import RolesCooEducacionDirectorCentroMaestroMixin

from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.forms.educacionForms.convivienteForm import ConvivienteFormEdit
from app.forms.educacionForms.viviendaForm import VivFormEdit
from app.models import Alumno, EstudiosAnt, Tutor, Religion_alumno, Apadecimiento, psicologico, vivienda, Conviviente, AspectosLab
from app.forms import AlumnoForm, TutorForm, EstAntForm, ReligionAlumnoForm, APadeForm, PsicoForm, VivForm, ConvivienteForm, LaboralForm
from django.db import IntegrityError, transaction
from django.forms import formset_factory
from django.shortcuts import redirect
from django.shortcuts import redirect

from app.models.educacion_model.padecimientoModel import Padecimiento

class AlumnoView(RolesCoordinadorEducacionYDirectorCentroMixin, generic.ListView):
    model = Alumno
    template_name = 'educacion/alumno_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            print('hola mundo')
            if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 5:
                return ["directorCentro/alumno_list.html"]

class AlumnoNew(LoginRequiredMixin, generic.CreateView):
    model = Alumno
    template_name = 'educacion/alumno_form.html'
    context_object_name = "obj"
    form_class = TutorForm
    second_form_class = EstAntForm
    third_form_class = AlumnoForm
    four_form_class = ReligionAlumnoForm
    five_form_class = formset_factory(APadeForm, extra=1)
    six_form_class = PsicoForm
    seven_form_class = VivForm
    eight_form_class = formset_factory(ConvivienteForm, extra=1)
    nine_form_class = LaboralForm
    success_url = reverse_lazy("educacion:alumno_list")
    login_url = 'app:login'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 5:
                return ["directorCentro/alumno_form.html"]
            elif self.request.user.user_profile.rol.id == 6:
                return ["maestro/alumno_form.html"]

    def get_context_data(self, **kwargs):
        context = super(AlumnoNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class()
        if 'form4' not in context:
            context['form4'] = self.four_form_class()
        if 'form5' not in context:

            context['form5'] = self.five_form_class(prefix = 'apadecimientos')
        if 'form6' not in context:
            context['form6'] = self.six_form_class()
        if 'form7' not in context:
            context['form7'] = self.seven_form_class()
        if 'form8' not in context:
            context['form8'] = self.eight_form_class(prefix = 'convivientes')
        if 'form9' not in context:
            context['form9'] = self.nine_form_class()
        context['errors_forms'] = {}
        
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Alumno, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        self.object = self.get_object
        form = self.form_class(request.POST,request.FILES)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST,request.FILES)
        form4 = self.four_form_class(request.POST)
        form5 = self.five_form_class(request.POST, prefix = 'apadecimientos')
        form6 = self.six_form_class(request.POST)
        form7 = self.seven_form_class(request.POST)
        form8 = self.eight_form_class(request.POST, prefix='convivientes')
        form9 = self.nine_form_class(request.POST)
        try:
            with transaction.atomic():
                if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid():
                    alumno = form3.save(commit=False)
                    alumno.estudios_anteriores = form2.save()
                    alumno.tutor = form.save()
                    alumno.save()
                    asplab = form9.save(commit=False)
                    asplab.alumno = alumno
                    asplab.save()
                    areligion = form4.save(commit=False)
                    areligion.alumno = alumno
                    areligion.save()
                    if len(form5.cleaned_data) == 1:
                        if form5.cleaned_data[0]:
                            for form_pad in form5:
                                apadecimiento=form_pad.save(commit=False)
                                apadecimiento.alumno = alumno
                                apadecimiento.save()
                    elif len(form5.cleaned_data) >= 1:
                        for form_pad in form5:
                            if form_pad.cleaned_data:
                                apadecimiento=form_pad.save(commit=False)
                                apadecimiento.alumno = alumno
                                apadecimiento.save()
                    psico=form6.save(commit=False)
                    psico.alumno = alumno
                    psico.save()
                    vivi= form7.save(commit=False)
                    vivi.estudiante=alumno
                    vivi.save()
                    for form_conviv in form8:
                        con= Conviviente(**form_conviv.cleaned_data, vivienda = vivi)
                        con.save()
                    print('creado')
                    if self.request.user.user_profile.rol.id == 6:
                        return redirect('educacion:home_maestro')

                    return HttpResponseRedirect(self.get_success_url())
                else:
                    #agregando los errores de cada form
                    print(form3.errors)
                    errors={
                        'form':{'erros':form.errors, 'name':'Tutor'},
                        'form2':{'erros':form2.errors, 'name':'Estudios Anteriores'},
                        'form3':{'erros':form3.errors, 'name':'Alumno'},
                        'form4':{'erros':form4.errors, 'name':'Religion'},
                        'form5':{'erros':form5.errors, 'name':'Apadecimiento'},
                        'form6':{'erros':form6.errors, 'name':'Psicologo'},
                        'form7':{'erros':form7.errors, 'name':'Vivienda'},
                        'form8':{'erros':form8.errors, 'name':'Convivientes'}
                    }
                    print(errors)
                    return self.render_to_response(self.get_context_data(form=form,
                        form2=form2,
                        form3=form3,
                        form4=form4,
                        form5=form5,
                        form6=form6,
                        form7=form7,
                        form8=form8,
                        errors_forms=errors
                        ))
        except IntegrityError:
           return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8))

class AlumnoEdit(RolesCoordinadorEducacionYDirectorCentroMixin, generic.UpdateView):
    model = Alumno
    template_name = "educacion/alumnoedit_form.html"
    context_object_name = "obj"
    form_class = AlumnoForm
    success_url = reverse_lazy("educacion:alumno_list")
    login_url = 'app:login'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 5:
                return ["directorCentro/alumnoedit_form.html"]

class AlumnoDetailAndCreate(RolesCoordinadorEducacionYDirectorCentroMixin, generic.UpdateView):
    template_name = "prueba/alumnoEdit.html"
    success_url = reverse_lazy("educacion:alumno_list")
    model = Alumno
    form_class = TutorForm
    second_form_class = EstAntForm
    third_form_class = AlumnoForm
    four_form_class = ReligionAlumnoForm
    five_form_class = APadeForm#formset_factory(APadeForm, extra=1)
    six_form_class = PsicoForm
    seven_form_class = VivForm
    eight_form_class = ConvivienteForm
    nine_form_class = LaboralForm

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 5:
                return ["directorCentro/alumnoEdit.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.third_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        alumno = self.get_object()
        apadecimientos = Apadecimiento.objects.filter(alumno=alumno)
        tutor = alumno.tutor
        estudios_anteriores = alumno.estudios_anteriores
        religion_alumno = alumno.R_alumno.first()
        analisis_psicologico = alumno.A_alumno.first()
        laboral = alumno.aspect_alumn.first()

        form = self.form_class(request.POST, request.FILES, instance = tutor)
        form2 = self.second_form_class(request.POST, instance= estudios_anteriores)
        form3 = self.third_form_class(request.POST, request.FILES, instance = alumno)
        form4 = self.four_form_class(request.POST, instance = religion_alumno)
        form6 = self.six_form_class(request.POST, instance = analisis_psicologico)
        form9 = self.nine_form_class(request.POST, instance = laboral)

        with transaction.atomic():
            for apadecimiento in apadecimientos:
                form5 = self.five_form_class(request.POST, instance = apadecimiento, prefix='apadecimientos')
                if form5.is_valid():
                    form5.save()
            if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form6.is_valid() and form9.is_valid():
                form3.save()
                form2.save()
                form.save()
                form4.save()
                form6.save()
                form9.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form9 = form9))

    def get(self, request, *args, **kwargs):
        alumno = self.get_object()
        tutor = alumno.tutor
        estudios_anteriores = alumno.estudios_anteriores
        religion_alumno = alumno.R_alumno.first()
        analisis_psicologico = alumno.A_alumno.first()
        vivienda = alumno.estudiante_vivieda.first()
        laboral = alumno.aspect_alumn.first()

        try:
            formApa = formset_factory(APadeForm, extra=0)
            listadoApa = []
            apadecimientos = Apadecimiento.objects.filter(alumno=alumno)

            for a in apadecimientos:
                listadoApa.append({
                    'padecimiento':a.padecimiento.id,
                    'tratamiento':a.tratamiento,
                    'estado_Alpadecimiento':a.estado_Alpadecimiento
                })
            formSetApa = formApa(initial=listadoApa, prefix = 'apadecimientos')
        except:
            print('ocurró un error')
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = tutor)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = estudios_anteriores)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance = alumno)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance = religion_alumno)
        if 'form5' not in context:
            context['form5'] = formSetApa
        if 'form6' not in context:
            context['form6'] = self.six_form_class(instance = analisis_psicologico)
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(instance = vivienda)
        if 'form9' not in context:
            context['form9'] = self.nine_form_class(instance = laboral)

        context['obj'] = ''
        context['alumno'] = self.get_object()

        return render(request, self.template_name, context)

class AlumnoEditViviendaConvivientes(RolesCoordinadorEducacionYDirectorCentroMixin, generic.UpdateView):
    template_name = "prueba/alumnoEditViviendaConvivientes.html"
    success_url = reverse_lazy("educacion:prueba_alumno_list_convivientes")
    model = Alumno
    form_viv = VivFormEdit
    form_convivientes = formset_factory(ConvivienteFormEdit, extra=1)

    def get_template_names(self):
            if self.template_name is None:
                raise ImproperlyConfigured(
                    "TemplateResponseMixin requires either a definition of "
                    "'template_name' or an implementation of 'get_template_names()'")
            else:
                if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                    return [self.template_name]
                elif self.request.user.user_profile.rol.id == 5:
                    return ["directorCentro/alumnoEditViviendaConvivientes.html"]

    def get(self, request, *args, **kwargs):
        alumno = self.get_object()
        vivienda = alumno.estudiante_vivieda.first()
        convivientes = Conviviente.objects.filter(vivienda=vivienda)
        context = {}
        context['form_viv'] = self.form_viv(instance = vivienda)
        context['convivientes'] = convivientes
        context['alumno'] = self.get_object()
        context['convivientes_form'] = self.form_convivientes(prefix = 'convivientes')

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        alumno = self.get_object()
        vivienda = alumno.estudiante_vivieda.first()
        form7 = VivFormEdit(request.POST, instance = vivienda)
        if form7.is_valid():
            form7.save()
            formNuevosConvivientes = self.form_convivientes(request.POST, prefix='convivientes')
            for form in formNuevosConvivientes:
                if form.is_valid():
                    data =  form.cleaned_data
                    if data:
                        Conviviente.objects.create(**data, vivienda = vivienda)
                        vivienda.cantidad_personas += 1
                        vivienda.save()
            return redirect('educacion:prueba_alumno', pk=self.get_object().id)
        else:
            return self.render_to_response(self.get_context_data(form7=form7))

class AlumnoDetail(RolesCooEducacionDirectorCentroMaestroMixin, generic.DetailView):
    template_name = "educacion/alumno_detail.html"
    model = Alumno

    def get_template_names(self):
            if self.template_name is None:
                raise ImproperlyConfigured(
                    "TemplateResponseMixin requires either a definition of "
                    "'template_name' or an implementation of 'get_template_names()'")
            else:
                if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                    return [self.template_name]
                elif self.request.user.user_profile.rol.id == 5:
                    return ["directorCentro/alumno_detail.html"]
                elif self.request.user.user_profile.rol.id == 6:
                    return ["maestro/alumno_detail.html"]

    def get_apadecimientos(self, alumno):
        return Apadecimiento.objects.filter(alumno=alumno)

    def get_convivientes(self, vivienda):
        return Conviviente.objects.filter(vivienda=vivienda)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alumno = self.get_object()
        vivienda = alumno.estudiante_vivieda.first()
        context['item'] = alumno
        context['tutor'] = alumno.tutor
        context['estudiosAnt'] =  alumno.estudios_anteriores
        context['relig'] = alumno.R_alumno.first()
        context['psic'] = alumno.A_alumno.first()
        context['viv'] = vivienda
        context['conviv'] = self.get_convivientes(vivienda)
        context['padec'] = self.get_apadecimientos(alumno)
        context['laboral'] = alumno.aspect_alumn.first()
        return context

class AlumnoDel(RolesCoordinadorEducacionYDirectorCentroMixin, generic.DeleteView):
    model = Alumno
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:alumno_list")

#rol para el maestro
class AlumnosDeCadaCurso(IsMaestroMixin, generic.ListView):
    model = Alumno
    template_name = 'maestro/listar_alumnos_por_curso.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_object(self):
        id_curso_grado = self.kwargs.get('pk')
        if id_curso_grado:
            return Ciclo_grado_curso.objects.filter(id=id_curso_grado).first()

    def get_queryset(self):
        return Alumno.objects.filter(estado_alumno=True, A_alumnos__ciclo_grado__cgc_cg__id = self.get_object().id)
