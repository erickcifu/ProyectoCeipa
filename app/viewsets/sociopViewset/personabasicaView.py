from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.models import PersonaBasica, GastoFamiliar, InfoEducacion, AspectosSalud, ViviendaSocio, ElectVivienda, PadresSociop, Encargado, InfoEconomica, Caract_laborales
from app.forms import PersonaBForm, GastFamForm, InfoEducacionForm, AspectosSaludForm, ViviendaSForm, ElectvivForm, PadresForm, EncargadoForm, InfoecoForm, ClabForm
from django.db import IntegrityError, transaction
from django.forms import formset_factory
from django.shortcuts import redirect

class PersonaBasicaView(LoginRequiredMixin, generic.ListView):
    model = PersonaBasica
    template_name = 'socioproductivo/personabasica_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PersonaBasicaNew(LoginRequiredMixin, generic.CreateView):
    model = PersonaBasica
    template_name = 'socioproductivo/personabasica_form.html'
    context_object_name = "obj"
    form_class = PersonaBForm
    second_form_class = formset_factory(GastFamForm, extra=1)
    third_form_class = formset_factory(InfoecoForm, extra=1)
    four_form_class = AspectosSaludForm
    five_form_class = ViviendaSForm
    six_form_class = formset_factory(ElectvivForm, extra=1)
    seven_form_class = PadresForm
    eight_form_class = EncargadoForm
    nine_form_class = InfoEducacionForm
    ten_form_class = ClabForm
    success_url = reverse_lazy("socioproductivo:personabasica_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super(PersonaBasicaNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(prefix = 'GastoFamiliars')
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'InfoEconomicas')
        if 'form4' not in context:
            context['form4'] = self.four_form_class(self.request.GET)
        if 'form5' not in context:
            context['form5'] = self.five_form_class(self.request.GET)
        if 'form6' not in context:
            context['form6'] = self.six_form_class(prefix = 'ElectViviendas')
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(self.request.GET)
        if 'form8' not in context:
            context['form8'] = self.eight_form_class(self.request.GET)
        if 'form9' not in context:
            context['form9'] = self.nine_form_class(self.request.GET)
        if 'form10' not in context:
            context['form10'] = self.ten_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(PersonaBasica, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        #try:
        with transaction.atomic():
            self.object = self.get_object
            form = self.form_class(request.POST,request.FILES)
            form2 = self.second_form_class(request.POST, prefix = 'GastoFamiliars')
            form3 = self.third_form_class(request.POST, prefix = 'InfoEconomicas')
            form4 = self.four_form_class(request.POST)
            form5 = self.five_form_class(request.POST)
            form6 = self.six_form_class(request.POST, prefix = 'ElectViviendas')
            form7 = self.seven_form_class(request.POST)
            form8 = self.eight_form_class(request.POST)
            form9 = self.nine_form_class(request.POST)
            form10 = self.ten_form_class(request.POST)
            if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid() and form10.is_valid():
                personab = form.save(commit=False)
                personab.vivienda_socio = form5.save()
                for form6_pad in form6:
                    ElectVivienda=form6_pad.save(commit=False)
                    print('ElectVivienda-----',ElectVivienda)
                    ElectVivienda.vivienda_socio = personab.vivienda_socio
                    ElectVivienda.save()
                personab.aspectos_salud =form4.save()
                personab.padres = form7.save()
                personab.tutor_socio = form8.save()
                personab.info_educacion= form9.save()
                personab.c_laborales = form10.save()
                personab.save()
                for form2_pad in form2:
                    Gastofamiliar=form2_pad.save(commit=False)
                    print('GastoFamiliar-----',GastoFamiliar)
                    GastoFamiliar.personab = personab
                    GastoFamiliar.save()
                for form3_pad in form3:
                    InfoEconomica=form3_pad.save(commit=False)
                    print('InfoEconomica-----',InfoEconomica)
                    InfoEconomica.personab = personab
                    InfoEconomica.save()

                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9 , form10=form10))
        #except IntegrityError:
            #handle_exception()


class PersonaBasicaEdit(LoginRequiredMixin, generic.UpdateView):
    model = PersonaBasica
    template_name = "socioproductivo/personabasica_form.html"
    context_object_name = "obj"
    form_class = PersonaBForm
    success_url = reverse_lazy("socioproductivo:personabasica_list")
    login_url = 'app:login'

class PersonaBasicaDel(LoginRequiredMixin, generic.DeleteView):
    model = PersonaBasica
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:personabasica_list")
