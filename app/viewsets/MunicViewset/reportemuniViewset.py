from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.db.models import Count, OuterRef, Subquery, IntegerField
from app.utils import render_to_pdf

from app.models import Beneficiado, Persona, IdiomaPersona, TutorMuni, Area, ComisionNA, GOrganizado, CorporacionMunicipal, PartidoPolitic, Maestro, LiderComunitario, CargoGrupo, MedioComuni, Tipo_medio, PadresFamilia
from app.models.educacion_model.idioma import idioma
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.departamento import departamento
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.genero import genero
from app.models import BeneficiadoArea


class AlumnosporDeptosView(ListView):
    model = Beneficiado
    template_name = 'reportespdf/participantes.html'
    context_object_name = 'obj'


class ListAlumnosDeptoPdf(View):

    def get(self, request, *args, **kwargs):
        beneficiado = Beneficiado.objects.filter(estado_beneficiado=True).count()
        depa = departamento.objects.filter(estado_departamento=True).annotate(cant = Count('M_dep__id'), cant_personas = Count('M_dep__P_muni__B_persona'))
        muni = municipio.objects.filter(estado_municipio=True).annotate( cantidad_municipio = Count('P_muni__B_persona'))
        per = Persona.objects.filter(estado_persona=True).count()
        privado = Beneficiado.objects.filter(estado_beneficiado=True, establecimiento_privado=True).values('persona__gen__genero').count()
        publico = Beneficiado.objects.filter(estado_beneficiado=True, establecimiento_publico=True).count()
        etni = etnia.objects.filter(estado_etnia=True).annotate(cantidad_total = Count('P_etnia__B_persona'))
        alumprim = Beneficiado.objects.filter(estado_beneficiado=True, nivel_primario=True).count()
        alumsecu = Beneficiado.objects.filter(estado_beneficiado=True, nivel_secundario=True).count()
        alumuniv = Beneficiado.objects.filter(estado_beneficiado=True, nivel_universitario=True).count()
        gen = genero.objects.filter(estado_genero=True).annotate(cant_per = Count('P_genero__B_persona'))
        area = Area.objects.annotate(cant_area = Count('ba_Area__beneficiado'))
        data = {
            'total_participantes': beneficiado,
            'Departamento': depa,
            'participantes_por_municipio': muni,
            'personas_total': per,
            'por_establecimiento_privado': privado,
            'por_establecimiento_publico': publico,
            'por_grupo_etnico': etni,
            'alumnos_primaria': alumprim,
            'alumnos_secundaria': alumsecu,
            'alumnos_universidad': alumuniv,
            'por_genero_municipio': gen,
            'cant_por_area': area
        }
        pdf = render_to_pdf('reportespdf/particip.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
        #return context

class total_corporacionesPDF(View):
    model = CorporacionMunicipal
    template_name = 'reportespdf/corporacion.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):

        corpto = CorporacionMunicipal.objects.filter(estado_corporacion=True).count()
        corpvac = CorporacionMunicipal.objects.filter(estado_corporacion=True, vacuna_corp=True).count()
        corpgen = genero.objects.filter(estado_genero=True).annotate(corp_genero = Count('P_genero__pers_comision'))
        corpetni = etnia.objects.filter(estado_etnia=True).annotate(corp_etnia = Count('P_etnia__pers_comision'))
        totalpart = CorporacionMunicipal.objects.filter(estado_corporacion=True, participacion=True).count
        partgrup = GOrganizado.objects.filter(estado_grupo=True).annotate( corp_grupo = Count('grupoO_cm'))
        partpoli = PartidoPolitic.objects.filter(estado=True).annotate( corp_partido = Count('partido_cm'))
        data = {
            'total_corp': corpto,
            'total_vacunados_corp': corpvac,
            'corporacion_por_genero': corpgen,
            'corp_por_etnia': corpetni,
            'total_part_gorg': totalpart,
            'part_por_grupo': partgrup,
            'por_part_politico': partpoli
        }
        pdf = render_to_pdf('reportespdf/corporacion.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class total_comisionesPDF(View):
    model = ComisionNA
    template_name = 'reportespdf/comisionees.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):

        totcom = ComisionNA.objects.filter(estado_comision=True).count()
        totcomvac = ComisionNA.objects.filter(estado_comision=True, vacuna_comision=True).count()
        porgen = genero.objects.filter(estado_genero=True).annotate( cant_gen = Count('P_genero__comision_pers'))
        cometni = etnia.objects.filter(estado_etnia=True).annotate( comision_etnia = Count('P_etnia__comision_pers'))
        totorg = ComisionNA.objects.filter(estado_comision=True, participacion_comina=True).count
        comorg = GOrganizado.objects.filter(estado_grupo=True).annotate( total_grupo = Count('gorga_comina'))
        secpublic = ComisionNA.objects.filter(estado_comision=True, inst_publica=True).count()
        serpriv = ComisionNA.objects.filter(estado_comision=True, inst_gobierno=True).count()

        data = {
            'total_comisiontes': totcom,
            'total_comisiones_vacuna': totcomvac,
            'por_genero': porgen,
            'comision_por_etnia': cometni,
            'total_grupo_organizado': totorg,
            'comision_grupo_org': comorg,
            'sector_publico': secpublic,
            'sector_privado': serpriv,
        }
        pdf = render_to_pdf('reportespdf/comisionees.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class Total_lideresPDF(View):
    model = LiderComunitario
    template_name = 'reportespdf/liderees.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):

        totlide = LiderComunitario.objects.filter(estado_liders=True).count()
        totlidvac = LiderComunitario.objects.filter(estado_liders=True, vacuna_covid_l=True).count()
        lidgen = genero.objects.filter(estado_genero=True).annotate( lideres_genero = Count('P_genero__B_personaM'))
        lidetni = etnia.objects.filter(estado_etnia=True).annotate(lideres_etnia=Count('P_etnia__B_personaM'))
        totlidgr = GOrganizado.objects.filter(estado_grupo=True).annotate( lideres_grupo = Count('G_organizado'))
        totlidcar = CargoGrupo.objects.filter(estado_cg=True).annotate(lideres_cargo = Count('C_cargoGM'))
        data = {
            'total_lideres': totlide,
            'total_lideres_vacunados': totlidvac,
            'lideres_por_genero': lidgen,
            'lideres_por_etnia': lidetni,
            'total_lideres_por_grupo': totlidgr,
            'total_lideres_por_cargo': totlidcar
        }
        pdf = render_to_pdf('reportespdf/liderees.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class total_maestrosPDF(View):
    model = Maestro
    template_name = 'reportespdf/maestroos.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):

        totmaes = Maestro.objects.filter(estado_maestro=True).count()
        totvacmaes = Maestro.objects.filter(estado_maestro=True, vacuna_covid=True).count()
        maesgen = genero.objects.filter(estado_genero=True).annotate(maestros_genero = Count('P_genero__M_persona'))
        maesetni = etnia.objects.filter(estado_etnia=True).annotate(maestros_etnia = Count('P_etnia__M_persona'))
        partmaesgru = Maestro.objects.filter(estado_maestro=True, Pargrupo=True).count()
        totmaesgrup = GOrganizado.objects.filter(estado_grupo=True).annotate( maestro_grupo = Count('M_cargoG'))
        maespublic = Maestro.objects.filter(estado_maestro=True, est_publico=True).count()
        maespriv = Maestro.objects.filter(estado_maestro=True, est_privado=True).count()
        maereaurb = Maestro.objects.filter(estado_maestro=True, area_urbana=True).count()
        maerearural = Maestro.objects.filter(estado_maestro=True, area_rural=True).count()

        data = {
            'total_maestros': totmaes,
            'total_vacunados_maestros': totvacmaes,
            'maestros_por_genero': maesgen,
            'maestros_por_etnia': maesetni,
            'part_maestro_grupo': partmaesgru,
            'total_maestros_por_grupo': totmaesgrup,
            'maestros_est_publico': maespublic,
            'maestros_est_privado': maespriv,
            'maestros_area_urbana': maereaurb,
            'maestro_area_rural': maerearural
        }
        pdf = render_to_pdf('reportespdf/maestroos.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class Total_mediosPDF(View):
    model = MedioComuni
    template_name = 'reportespdf/medioos.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):
        totmedi = MedioComuni.objects.filter(estado=True).count()
        totmedvac = MedioComuni.objects.filter(estado=True, vacuna_medio=True).count()
        medporgen = genero.objects.annotate(medios_genero=Count('P_genero__P_personaM'))
        medporetni = etnia.objects.annotate(medios_etnia=Count('P_etnia__P_personaM'))
        portipmed = Tipo_medio.objects.annotate(medios_tipo = Count('tipo_med'))
        data = {
                'total_medios': totmedi,
                'total_medios_vacunados': totmedvac,
                'medios_por_genero': medporgen,
                'medios_por_etnia': medporetni,
                'por_tipo_medio': portipmed
            }
        pdf = render_to_pdf('reportespdf/medioos.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class Total_padresPDF(View):
    model = PadresFamilia
    template_name = 'reportespdf/padrees.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):

        totpadre = PadresFamilia.objects.filter(estado_padres=True).count()
        totpavac = PadresFamilia.objects.filter(estado_padres=True, vacunaCovid=True).count()
        padrgen = genero.objects.filter(estado_genero=True).annotate(padres_genero = Count('P_genero__per_padre'))
        padetni = etnia.objects.filter(estado_etnia=True).annotate(etnia_padres = Count('P_etnia__per_padre'))
        parpadgru = PadresFamilia.objects.filter(estado_padres=True, participacionG=True).count()
        padgrup = GOrganizado.objects.filter(estado_grupo=True).annotate(padres_grupo=Count('grupoOr_padre'))
        leeandscrib = PadresFamilia.objects.filter(estado_padres=True, leer_P=True, escribir_p=True).count()
        soleer = PadresFamilia.objects.filter(estado_padres=True, leer_P=True, escribir_p=False).count()
        solescrib = PadresFamilia.objects.filter(estado_padres=True, escribir_p=True, leer_P=True).count()
        noleescrib = PadresFamilia.objects.filter(estado_padres=True, escribir_p=False, leer_P=False).count()
        data = {
                'total_padres': totpadre,
                'total_padres_vacunados': totpavac,
                'padres_por_genero': padrgen,
                'padres_por_etnia': padetni,
                'part_padres_grupo': parpadgru,
                'padres_por_grupo': padgrup,
                'leer_y_escribir': leeandscrib,
                'solo_leer': soleer,
                'solo_escribir': solescrib,
                'no_leer_no_escribir': noleescrib
            }
        pdf = render_to_pdf('reportespdf/padrees.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
