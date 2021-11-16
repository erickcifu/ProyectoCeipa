from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Count, OuterRef, Subquery, IntegerField

from app.models import Beneficiado, Persona, IdiomaPersona, TutorMuni, Area, ComisionNA, GOrganizado, CorporacionMunicipal, PartidoPolitic, Maestro, LiderComunitario, CargoGrupo, MedioComuni, Tipo_medio, PadresFamilia
from app.models.educacion_model.idioma import idioma
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.departamento import departamento
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.genero import genero
from app.models import BeneficiadoArea

class AlumnosporDepto(LoginRequiredMixin, generic.ListView):
    model = Beneficiado
    template_name = 'reportes/participantes.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_participantes'] = Beneficiado.objects.filter(estado_beneficiado=True).count()
        context['Departamento'] = departamento.objects.filter(estado_departamento=True).annotate(cant = Count('M_dep__id'), cant_personas = Count('M_dep__P_muni__B_persona'))
        context['participantes_por_municipio'] = municipio.objects.filter(estado_municipio=True).annotate( cantidad_municipio = Count('P_muni__B_persona'))
        context['personas_total'] = Persona.objects.filter(estado_persona=True).count()
        context['por_establecimiento_privado'] = Beneficiado.objects.filter(estado_beneficiado=True, establecimiento_privado=True).values('persona__gen__genero').count()
        context['por_establecimiento_publico'] = Beneficiado.objects.filter(estado_beneficiado=True, establecimiento_publico=True).count()
        context['por_grupo_etnico'] = etnia.objects.filter(estado_etnia=True).annotate(cantidad_total = Count('P_etnia__B_persona'))
        context['alumnos_primaria'] = Beneficiado.objects.filter(estado_beneficiado=True, nivel_primario=True).count()
        context['alumnos_secundaria'] = Beneficiado.objects.filter(estado_beneficiado=True, nivel_secundario=True).count()
        context['alumnos_universidad'] = Beneficiado.objects.filter(estado_beneficiado=True, nivel_universitario=True).count()
        context['por_genero_municipio'] = genero.objects.filter(estado_genero=True).annotate(cant_per = Count('P_genero__B_persona'))
        context['cant_por_area'] = Area.objects.annotate(cant_area = Count('ba_Area__beneficiado'))

        return context

class total_comisiones(LoginRequiredMixin, generic.ListView):
    model = ComisionNA
    template_name = 'reportes/comisiones.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_comisiontes'] = ComisionNA.objects.filter(estado_comision=True).count()
        context['total_comisiones_vacuna'] = ComisionNA.objects.filter(estado_comision=True, vacuna_comision=True).count()
        context['por_genero'] = genero.objects.filter(estado_genero=True).annotate( cant_gen = Count('P_genero__comision_pers'))
        context['comision_por_etnia'] = etnia.objects.filter(estado_etnia=True).annotate( comision_etnia = Count('P_etnia__comision_pers'))
        context['total_grupo_organizado'] = ComisionNA.objects.filter(estado_comision=True, participacion_comina=True).count
        context['comision_grupo_org'] = GOrganizado.objects.filter(estado_grupo=True).annotate( total_grupo = Count('gorga_comina'))
        context['sector_publico'] = ComisionNA.objects.filter(estado_comision=True, inst_publica=True).count()
        context['sector_privado'] = ComisionNA.objects.filter(estado_comision=True, inst_gobierno=True).count()
        return context

class total_corporaciones(LoginRequiredMixin, generic.ListView):
    model = CorporacionMunicipal
    template_name = 'reportes/corporaciones.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_corp'] = CorporacionMunicipal.objects.filter(estado_corporacion=True).count()
        context['total_vacunados_corp'] = CorporacionMunicipal.objects.filter(estado_corporacion=True, vacuna_corp=True).count()
        context['corporacion_por_genero'] = genero.objects.filter(estado_genero=True).annotate(corp_genero = Count('P_genero__pers_comision'))
        context['corp_por_etnia'] = etnia.objects.filter(estado_etnia=True).annotate(corp_etnia = Count('P_etnia__pers_comision'))
        context['total_part_gorg'] = CorporacionMunicipal.objects.filter(estado_corporacion=True, participacion=True).count
        context['part_por_grupo'] = GOrganizado.objects.filter(estado_grupo=True).annotate( corp_grupo = Count('grupoO_cm'))
        context['por_part_politico'] = PartidoPolitic.objects.filter(estado=True).annotate( corp_partido = Count('partido_cm'))
        return context

class total_maestros(LoginRequiredMixin, generic.ListView):
    model = Maestro
    template_name = 'reportes/maestros.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_maestros'] = Maestro.objects.filter(estado_maestro=True).count()
        context['total_vacunados_maestros'] = Maestro.objects.filter(estado_maestro=True, vacuna_covid=True).count()
        context['maestros_por_genero'] = genero.objects.filter(estado_genero=True).annotate(maestros_genero = Count('P_genero__M_persona'))
        context['maestros_por_etnia'] = etnia.objects.filter(estado_etnia=True).annotate(maestros_etnia = Count('P_etnia__M_persona'))
        context['part_maestro_grupo'] = Maestro.objects.filter(estado_maestro=True, Pargrupo=True).count()
        context['total_maestros_por_grupo'] = GOrganizado.objects.filter(estado_grupo=True).annotate( maestro_grupo = Count('M_cargoG'))
        context['maestros_est_publico'] = Maestro.objects.filter(estado_maestro=True, est_publico=True).count()
        context['maestros_est_privado'] = Maestro.objects.filter(estado_maestro=True, est_privado=True).count()
        context['maestros_area_urbana'] = Maestro.objects.filter(estado_maestro=True, area_urbana=True).count()
        context['maestro_area_rural'] = Maestro.objects.filter(estado_maestro=True, area_rural=True).count()
        return context

class Total_lideres(LoginRequiredMixin, generic.ListView):
    model = LiderComunitario
    template_name = 'reportes/lideres.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_lideres'] = LiderComunitario.objects.filter(estado_liders=True).count()
        context['total_lideres_vacunados'] = LiderComunitario.objects.filter(estado_liders=True, vacuna_covid_l=True).count()
        context['lideres_por_genero'] = genero.objects.filter(estado_genero=True).annotate( lideres_genero = Count('P_genero__B_personaM'))
        context['lideres_por_etnia'] = etnia.objects.filter(estado_etnia=True).annotate(lideres_etnia=Count('P_etnia__B_personaM'))
        context['total_lideres_por_grupo'] = GOrganizado.objects.filter(estado_grupo=True).annotate( lideres_grupo = Count('G_organizado'))
        context['total_lideres_por_cargo'] = CargoGrupo.objects.filter(estado_cg=True).annotate(lideres_cargo = Count('C_cargoGM'))
        return context

class Total_medios(LoginRequiredMixin, generic.ListView):
    model = MedioComuni
    template_name = 'reportes/medios.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_medios'] = MedioComuni.objects.filter(estado=True).count()
        context['total_medios_vacunados'] = MedioComuni.objects.filter(estado=True, vacuna_medio=True).count()
        context['medios_por_genero'] = genero.objects.annotate(medios_genero=Count('P_genero__P_personaM'))
        context['medios_por_etnia'] = etnia.objects.annotate(medios_etnia=Count('P_etnia__P_personaM'))
        context['por_tipo_medio'] = Tipo_medio.objects.annotate(medios_tipo = Count('tipo_med'))
        return context

class Total_padres(LoginRequiredMixin, generic.ListView):
    model = PadresFamilia
    template_name = 'reportes/padres.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_padres'] = PadresFamilia.objects.filter(estado_padres=True).count()
        context['total_padres_vacunados'] = PadresFamilia.objects.filter(estado_padres=True, vacunaCovid=True).count()
        context['padres_por_genero'] = genero.objects.filter(estado_genero=True).annotate(padres_genero = Count('P_genero__per_padre'))
        context['padres_por_etnia'] = etnia.objects.filter(estado_etnia=True).annotate(etnia_padres = Count('P_etnia__per_padre'))
        context['part_padres_grupo'] = PadresFamilia.objects.filter(estado_padres=True, participacionG=True).count()
        context['padres_por_grupo'] = GOrganizado.objects.filter(estado_grupo=True).annotate(padres_grupo=Count('grupoOr_padre'))
        context['leer_y_escribir'] = PadresFamilia.objects.filter(estado_padres=True, leer_P=True, escribir_p=True).count()
        context['solo_leer'] = PadresFamilia.objects.filter(estado_padres=True, leer_P=True, escribir_p=False).count()
        context['solo_escribir'] = PadresFamilia.objects.filter(estado_padres=True, escribir_p=True, leer_P=True).count()
        context['no_leer_no_escribir'] = PadresFamilia.objects.filter(estado_padres=True, escribir_p=False, leer_P=False).count()
        return context
