from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.models import PersonaBasica, GastoFamiliar, InfoEducacion, AspectosSalud, ViviendaSocio, ElectVivienda, PadresSociop, Encargado, InfoEconomica, Caract_laborales, Taller, Inscripcionp
from app.forms import PersonaBForm, GastFamForm, InfoEducacionForm, AspectosSaludForm, ViviendaSForm, ElectvivForm, PadresForm, EncargadoForm, InfoecoForm, ClabForm
from django.db import IntegrityError, transaction
from django.forms import formset_factory
from django.shortcuts import redirect

class PersonaBasicaView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = PersonaBasica
    template_name = 'socioproductivo/personabasica_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PersonaBasicaNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
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

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 10 or user == 11:
                return [self.template_name]
            elif user == 12:
                return ["equipoSocioproductivo/personabasica_form.html"]
            else:
                return [self.template_name]

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
        try:
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
                        ElectVivienda.vivienda = personab.vivienda_socio
                        ElectVivienda.save()
                    personab.aspectos_salud =form4.save()
                    personab.padres = form7.save()
                    personab.tutor_socio = form8.save()
                    personab.info_educacion= form9.save()
                    personab.caract_laborales = form10.save()
                    personab.save()
                    for form2_pad in form2:
                        gasto=form2_pad.save(commit=False)
                        print('GastoFamiliar-----',GastoFamiliar)
                        gasto = GastoFamiliar(**form2_pad.cleaned_data, gasto_persona = personab)
                        gasto.save()
                    for form3_pad in form3:
                        InfoEconomica=form3_pad.save(commit=False)
                        print('InfoEconomica-----',InfoEconomica)
                        InfoEconomica.eco_persona = personab
                        InfoEconomica.save()

                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9 , form10=form10))
        except IntegrityError:
            handle_exception()


class PersonaBasicaEdit(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.UpdateView):
    model = PersonaBasica
    template_name = "socioproductivo/personabasica_edit.html"
    form_class = PersonaBForm
    second_form_class = GastFamForm #formset_factory(GastFamForm, extra=1)
    third_form_class = InfoecoForm #formset_factory(InfoecoForm, extra=1)
    four_form_class = AspectosSaludForm
    five_form_class = ViviendaSForm
    six_form_class = ElectvivForm #formset_factory(ElectvivForm, extra=1)
    seven_form_class = PadresForm
    eight_form_class = EncargadoForm
    nine_form_class = InfoEducacionForm
    ten_form_class = ClabForm
    success_url = reverse_lazy("socioproductivo:personabasica_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        personab = self.get_object()
        gastos_fam = GastoFamiliar.objects.filter(gasto_persona = personab)
        info_eco = InfoEconomica.objects.filter(eco_persona = personab)
        padres = personab.padres
        info_salud = personab.aspectos_salud
        info_educacion = personab.info_educacion
        info_laboral = personab.aspectos_salud
        tutor_socio = personab.tutor_socio
        vivienda = personab.vivienda_socio

        form = self.form_class(request.POST, request.FILES, instance = personab)
        form4 = self.four_form_class(request.POST, instance = info_salud)
        form5 = self.five_form_class(request.POST, instance = vivienda)
        form7 = self.seven_form_class(request.POST, instance = padres)
        form8 = self.eight_form_class(request.POST, instance = tutor_socio)
        form9 = self.nine_form_class(request.POST, instance = info_educacion)
        form10 = self.nine_form_class(request.POST, instance = info_laboral)

        with transaction.atomic():
            for eco_info in info_eco:
                form3 = self.third_form_class(request.POST, instance=eco_info, prefix='InfoEconomicas')
                if form3.is_valid():
                    form3.save()
            for gastos in gastos_fam:
                form2 = self.second_form_class(request.POST, instance = gastos_fam, prefix = 'GastoFamiliars')
                if form2.is_valid():
                    form2.save()
            if form.is_valid() and form4.is_valid() and form7.is_valid() and form8.is_valid() and form9.is_valid() and form10.is_valid():
                form.save()
                form4.save()
                form5.save()
                form7.save()
                form8.save()
                form9.save()
                form10.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form4=form4, form5=form5, form7 = form7, form8=form8, form9=form9, form10=form10))

    def get(self, request, *args, **kwargs):
        personab = self.get_object()
        padres = personab.padres
        info_salud = personab.aspectos_salud
        info_educacion = personab.info_educacion
        info_laboral = personab.aspectos_salud
        tutor_socio = personab.tutor_socio
        vivienda = personab.vivienda_socio

        try:
            form_eco = formset_factory(InfoecoForm, extra=0)
            listadoEco = []
            eco_info = InfoEconomica.objects.filter(eco_persona = personab)

            for a in eco_info:
                listadoEco.append({
                    'pariente': a.pariente,
                    'cantidad_mensual': a.cantidad_mensual,
                    'procedencia_ingreso': a.procedencia_ingreso,
                    'observacion': a.observacion,
                    'estado_infoeco': a.estado_infoeco,
                })
            formsetEco = form_eco(initial=listadoEco, prefix='InfoEconomicas')
        except:
            print('ocurró un error')
            return HttpResponseRedirect(self.success_url)

        try:
            form_gastos = formset_factory(GastoFamiliar, extra=0)
            listadoGastos = []
            gastos_info = GastoFamiliar.objects.filter(gasto_persona = personab)

            for b in gastos_info:
                listadoGastos.append({
                    'servicio': a.servicio,
                    'cantidad_servicio': a.cantidad_servicio,
                    'estado_gastofamiliar': a.estado_gastofamiliar,
                })
            formsetGastos = form_gastos(initial=listadoGastos, prefix='GastoFamiliars')
        except:
            print('ocurró un error')
            return HttpResponseRedirect(self.success_url)

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = personab)
        if 'form2' not in context:
            context['form2'] = formsetGastos
        if 'form3' not in context:
            context['form3'] = formsetEco
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance = info_salud)
        if 'form5' not in context:
            context['form5'] = self.five_form_class(vivienda)
        if 'form7' not in context:
            context['form7'] = self.seven_form_class(instance = padres)
        if 'form8' not in context:
            context['form8'] = self.eight_form_class(instance = tutor_socio)
        if 'form9' not in context:
            context['form9'] = self.nine_form_class(instance = info_educacion)
        if 'form10' not in context:
            context['form10'] = self.ten_form_class(instance = info_laboral)

        context['obj'] = ''
        context['personab'] = self.get_object()

        return render(request, self.template_name, context)

class personabDetail(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.DetailView):
    template_name = "socioproductivo/personab_detail.html"
    model = PersonaBasica

    def get_ElectVivienda(self, vivienda):
        return ElectVivienda.objects.filter(vivienda=vivienda)

    def get_InfoEconomica(self, personab):
        return InfoEconomica.objects.filter(eco_persona=personab)

    def get_GastoFamiliar(self, personab):
        return GastoFamiliar.objects.filter(gasto_persona=personab)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personab = self.get_object()
        vivienda = personab.vivienda_socio
        context['item'] = personab
        context['padres'] = personab.padres
        context['aspect_salud'] = personab.aspectos_salud
        context['info_educacion'] =  personab.info_educacion
        context['caract_laborales'] = personab.caract_laborales
        context['tutor_socio'] = personab.tutor_socio
        context['viv'] = vivienda
        context['electrodomesticos_vivienda'] = self.get_ElectVivienda(vivienda)
        context['info_eco'] = self.get_InfoEconomica(personab)
        context['gasto_familiar'] = self.get_GastoFamiliar(personab)
        return context

class PersonaBasicaDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = PersonaBasica
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:personabasica_list")

class ListarParticipantesPorTaller(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.ListView):
    model = PersonaBasica
    template_name = "socioproductivo/participantes_por_taller.html"
    context_object_name = "obj"

    def get_queryset(self):
        id_taller = self.request.GET.get("id_taller")
        if id_taller:
            return PersonaBasica.objects.filter(ins_per__taller_id=int(id_taller))
        return PersonaBasica.objects.filter(ins_per__taller_id__in=Taller.objects.filter(estado_taller=True).values_list('id'))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['talleres'] = Taller.objects.all()
        id_taller = None
        try:
            id_taller = Taller.objects.filter(id=int(self.request.GET.get("id_taller"))).first()
        except:
            id_taller = None
        context['id_taller'] = id_taller
        return context

class ListarParticipantesCertificados(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.ListView):
    model = Inscripcionp
    template_name = "socioproductivo/participantes_para_formlab.html"
    context_object_name = "obj"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['participantes_certificados'] = Inscripcionp.objects.filter(certificado_taller=True)
        return context
