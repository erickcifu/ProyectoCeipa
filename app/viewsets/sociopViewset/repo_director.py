from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Count, OuterRef, Subquery, IntegerField
from app.viewsets.users.directorGeneral.mixin import IsDirectorGeneralMixin

from app.models import FormacionLab, PersonaBasica, FormacionLab, Emprendimiento, ViviendaSocio, Caract_laborales
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.departamento import departamento
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.genero import genero

class ParticipantesSociop_direc(IsDirectorGeneralMixin, generic.ListView):
    model = PersonaBasica
    template_name = 'directorGeneral/sociop.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleabilidad'] = FormacionLab.objects.filter(formacion_completada=True).count()
        context['emprendimientos'] = Emprendimiento.objects.filter(estado_Emprendimiento=True).count()
        context['sociop_po_genero'] = genero.objects.filter(estado_genero=True).annotate(socio_genero = Count('PB_genero'))
        context['emp_por_muni'] = municipio.objects.filter(estado_municipio=True).annotate( cantidad_municipio = Count('Em_muni'))
        context['emp_por_dep'] = departamento.objects.filter(estado_departamento=True).annotate( dep_sociop = Count('M_dep__PB_municipio'))
        context['edad'] = PersonaBasica.objects.filter(estado_persona_basica=True).values('edad').count()
        context['estrato_pobre'] = ViviendaSocio.objects.filter(estado_vivsocio=True, pobre=True).count()
        context['estrato_no_pobre'] = ViviendaSocio.objects.filter(estado_vivsocio=True, no_pobre = True).count()
        context['estrato_extr_pobre'] = ViviendaSocio.objects.filter(estado_vivsocio=True, Extemadamente_pobre = True).count()
        context['socio_grupo_etn'] = etnia.objects.filter(estado_etnia=True).annotate(socio_etnia = Count('PB_etnia'))
        context['total_migraciones'] = Caract_laborales.objects.filter(s_americano=True).count()
        context['total_no_migrar'] = Caract_laborales.objects.filter(s_americano=False).count()
        return context
