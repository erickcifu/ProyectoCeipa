from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.db.models import Count, OuterRef, Subquery, IntegerField
from app.utils import render_to_pdf


from app.models import FormacionLab, PersonaBasica, FormacionLab, Emprendimiento, ViviendaSocio, Caract_laborales
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.departamento import departamento
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.genero import genero

class ParticipantesSociopdf(View):
    model = PersonaBasica
    template_name = 'reportes/sociopdf.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):
        empleabilidad = FormacionLab.objects.filter(formacion_completada=True).count()
        emprendimientos = Emprendimiento.objects.filter(estado_Emprendimiento=True).count()
        sociop_po_genero = genero.objects.filter(estado_genero=True).annotate(socio_genero = Count('PB_genero'))
        emp_por_muni = municipio.objects.filter(estado_municipio=True).annotate( cantidad_municipio = Count('Em_muni'))
        emp_por_dep = departamento.objects.filter(estado_departamento=True).annotate( dep_sociop = Count('M_dep__PB_municipio'))
        edad = PersonaBasica.objects.filter(estado_persona_basica=True).values('edad').count()
        estrato_pobre = ViviendaSocio.objects.filter(estado_vivsocio=True, pobre=True).count()
        estrato_no_pobre = ViviendaSocio.objects.filter(estado_vivsocio=True, no_pobre = True).count()
        estrato_extr_pobre = ViviendaSocio.objects.filter(estado_vivsocio=True, Extemadamente_pobre = True).count()
        socio_grupo_etn = etnia.objects.filter(estado_etnia=True).annotate(socio_etnia = Count('PB_etnia'))
        total_migraciones = Caract_laborales.objects.filter(s_americano=True).count()
        total_no_migrar = Caract_laborales.objects.filter(s_americano=False).count()

        data = {
            'empleabilidad': empleabilidad,
            'emprendimientos': emprendimientos,
            'sociop_po_genero': sociop_po_genero,
            'emp_por_muni': emp_por_muni,
            'emp_por_dep': emp_por_dep,
            'edad': edad,
            'estrato_pobre': estrato_pobre,
            'estrato_no_pobre': estrato_no_pobre,
            'estrato_extr_pobre': estrato_extr_pobre,
            'socio_grupo_etn': socio_grupo_etn,
            'total_migraciones': total_migraciones,
            'total_no_migrar': total_no_migrar
        }
        pdf_sociop = render_to_pdf('reportespdf/sociopdf.html', data)
        return HttpResponse(pdf_sociop, content_type='application/pdf')
