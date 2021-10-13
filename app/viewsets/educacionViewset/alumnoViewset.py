from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.models import Alumno, EstudiosAnt, Tutor, Religion_alumno, Apadecimiento, psicologico, vivienda, Conviviente
from app.forms import AlumnoForm, TutorForm, EstAntForm, ReligionAlumnoForm, APadeForm, PsicoForm, VivForm, ConvivienteForm
from django.db import IntegrityError, transaction

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
    five_form_class = APadeForm
    six_form_class = PsicoForm
    seven_form_class = VivForm
    eight_form_class = ConvivienteForm
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
            context['form5'] = self.five_form_class(self.request.GET)
        if 'form6' not in context:
            context['form6'] = self.six_form_class(self.request.GET)
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(self.request.GET)
        if 'form8' not in context:
            context['form8'] = self.eight_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Alumno, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST)
                form4 = self.four_form_class(request.POST)
                form5 = self.five_form_class(request.POST)
                form6 = self.six_form_class(request.POST)
                form7 = self.seven_form_class(request.POST)
                form8 = self.eight_form_class(request.POST)

                if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid():
                    alumno = form3.save(commit=False)
                    alumno.estudios_anteriores = form2.save()
                    alumno.tutor = form.save()
                    alumno.save()
                    areligion = form4.save(commit=False)
                    areligion.alumno = alumno
                    areligion.save()
                    apadecimiento=form5.save(commit=False)
                    apadecimiento.alumno = alumno
                    apadecimiento.save()
                    psico=form6.save(commit=False)
                    psico.alumno = alumno
                    psico.save()
                    vivi= form7.save(commit=False)
                    vivi.estudiante=alumno
                    vivi.save()
                    con= form8.save(commit=False)
                    con.vivienda=vivi
                    con.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8))
        except IntegrityError:
            handle_exception()


class AlumnoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Alumno
    template_name = "educacion/alumnoedit_form.html"
    context_object_name = "obj"
    form_class = AlumnoForm
    success_url = reverse_lazy("educacion:alumno_list")
    login_url = 'app:login'


class AlumnoDel(LoginRequiredMixin, generic.DeleteView):
    model = Alumno
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:alumno_list")
