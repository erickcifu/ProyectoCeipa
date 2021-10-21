from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
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

class AlumnoView(LoginRequiredMixin, generic.ListView):
    model = Alumno
    template_name = 'educacion/alumno_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

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

    def get_context_data(self, **kwargs):
        context = super(AlumnoNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(self.request.GET)
        if 'form5' not in context:

            context['form5'] = self.five_form_class(prefix = 'apadecimientos')
        if 'form6' not in context:
            context['form6'] = self.six_form_class(self.request.GET)
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(self.request.GET)
        if 'form8' not in context:
            context['form8'] = self.eight_form_class(prefix = 'convivientes')
        if 'form9' not in context:
            context['form9'] = self.nine_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Alumno, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
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
                    for form_pad in form5:
                        apadecimiento=form_pad.save(commit=False)
                        print('apadecimiento-----',apadecimiento)
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
                        print('convivientes-----',con)
                        con.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9))
        except IntegrityError:
            handle_exception()


class AlumnoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Alumno
    template_name = "educacion/alumnoedit_form.html"
    context_object_name = "obj"
    form_class = AlumnoForm
    success_url = reverse_lazy("educacion:alumno_list")
    login_url = 'app:login'

class AlumnoDetailAndCreate(LoginRequiredMixin, generic.UpdateView):
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

        form = self.form_class(request.POST, request.FILES, instance = tutor)
        form2 = self.second_form_class(request.POST, instance= estudios_anteriores)
        form3 = self.third_form_class(request.POST, request.FILES, instance = alumno)
        form4 = self.four_form_class(request.POST, instance = religion_alumno)
        form6 = self.six_form_class(request.POST, instance = analisis_psicologico)

        with transaction.atomic():
            for apadecimiento in apadecimientos:
                form5 = self.five_form_class(request.POST, instance = apadecimiento, prefix='apadecimientos')
                if form5.is_valid():
                    form5.save()
            if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form6.is_valid():
                form3.save()
                form2.save()
                form.save()
                form4.save()
                form6.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6))

    def get(self, request, *args, **kwargs):
        alumno = self.get_object()
        tutor = alumno.tutor
        estudios_anteriores = alumno.estudios_anteriores
        religion_alumno = alumno.R_alumno.first()
        analisis_psicologico = alumno.A_alumno.first()
        vivienda = alumno.estudiante_vivieda.first()

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

        context['obj'] = ''
        context['alumno'] = self.get_object()

        return render(request, self.template_name, context)

class AlumnoEditViviendaConvivientes(LoginRequiredMixin, generic.UpdateView):
    template_name = "prueba/alumnoEditViviendaConvivientes.html"
    success_url = reverse_lazy("educacion:prueba_alumno_list_convivientes")
    model = Alumno
    form_viv = VivFormEdit
    form_convivientes = formset_factory(ConvivienteFormEdit, extra=1)

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

class AlumnoDetail(LoginRequiredMixin, generic.DetailView):
    template_name = "educacion/alumno_detail.html"
    model = Alumno

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

        return context


class AlumnoDel(LoginRequiredMixin, generic.DeleteView):
    model = Alumno
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:alumno_list")
