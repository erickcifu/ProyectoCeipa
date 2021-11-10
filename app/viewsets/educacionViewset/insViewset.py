from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.directorCentro.mixin import IsDirectorCentroMixin
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin

from app.models import Inscripcion, Alumno, centro_educativo, Ciclo_grado, Ciclo
from app.forms import InsForm
from datetime import datetime

from app.models.educacion_model.ciclo import Ciclo

class InsView(LoginRequiredMixin, generic.ListView):
    model = Inscripcion
    template_name = 'educacion/ins_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class InsNew(LoginRequiredMixin, generic.CreateView):
    model = Inscripcion
    template_name = "educacion/ins_form.html"
    context_object_name = "obj"
    form_class = InsForm
    success_url = reverse_lazy("educacion:ins_list")
    login_url = 'app:login'

class InsEdit(LoginRequiredMixin, generic.UpdateView):
    model = Inscripcion
    template_name = "educacion/ins_form.html"
    context_object_name = "obj"
    form_class = InsForm
    success_url = reverse_lazy("educacion:ins_list")
    login_url = 'app:login'

class InsDel(LoginRequiredMixin, generic.DeleteView):
    model = Inscripcion
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:ins_list")

#listando los maestros por centro educativo
class ListarAlumnosPorCentroEducativo(IsCoordinadorEducacionMixin, generic.ListView):
    model = Alumno
    template_name = 'educacion/alumnos_list_por_centro_educativo.html'
    context_object_name = 'obj'

    def get_queryset(self):
        id_centro_educativo = self.request.GET.get("id_centro_educativo")
        if id_centro_educativo:
            return Alumno.objects.filter(A_alumnos__centro_educativo_id=int(id_centro_educativo))

        return Alumno.objects.filter(A_alumnos__centro_educativo_id__in=centro_educativo.objects.filter(estado_centro=True).values_list('id'))


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['centros_educativos'] = centro_educativo.objects.all()
        id_centro_educativo = None
        try:
            id_centro_educativo = centro_educativo.objects.filter(id=int(self.request.GET.get("id_centro_educativo"))).first()
        except:
            id_centro_educativo = None
        context['id_centro_educativo'] =  id_centro_educativo
        return context

class ListarGradosParaInscribirAlumnos(IsCoordinadorEducacionMixin, generic.ListView):
    model = Ciclo_grado
    template_name = 'educacion/cg_list_para_inscribir_alumnos.html'
    context_object_name = 'obj'
    login_url = 'app:login'
    queryset = Ciclo_grado.objects.order_by('ciclo', 'seccion')

    def get_queryset(self):
        existe_ciclo = Ciclo.objects.filter(estado_ciclo=True, anio = datetime.now().year).first()
        if existe_ciclo:
            return Ciclo_grado.objects.filter(estado_cg=True, ciclo=existe_ciclo).order_by('ciclo','seccion')
        return None

    def get_object(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        if id_centro_educativo:
            return centro_educativo.objects.filter(id=int(id_centro_educativo)).first()
        return None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context['id_centro_educativo'] =  self.get_object()
        return context

class InscribirAlumnos(IsCoordinadorEducacionMixin, generic.CreateView):
    model = Inscripcion
    template_name = 'educacion/alumnoInscripcionPorGrado.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_centro_educativo(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        if id_centro_educativo:
            return centro_educativo.objects.filter(id=int(id_centro_educativo)).first()
        return None

    def get_grado(self):
        id_grado = self.kwargs.get('id_grado')
        if id_grado:
            return Ciclo_grado.objects.filter(id=int(id_grado)).first()
        return None

    def get_grados(self):
        if self.kwargs.get('id_grado'):

            existe_ciclo = Ciclo.objects.filter(estado_ciclo=True, anio = datetime.now().year).first()
            grados = Ciclo_grado.objects.filter(estado_cg=True, ciclo=existe_ciclo).values_list('id')
            print(grados)
            return grados
        return []

    def get_centros_educativos(self):
        if self.kwargs.get('id_centro_educativo'):
            return centro_educativo.objects.filter(estado_centro=True).values_list('id')
        return []


    def get(self, request, *args, **kwargs):
        id_centro = self.get_centro_educativo()
        id_grado = self.get_grado()
        context={}
        context['id_centro_educativo'] =  id_centro
        context['id_grado'] = id_grado
        context['alumnos'] = Alumno.objects.filter(estado_alumno=True).exclude(A_alumnos__centro_educativo_id = id_centro.id, A_alumnos__ciclo_grado_id = id_grado.id)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id_centro = self.get_centro_educativo()
        id_grado = self.get_grado()
        alumnos = self.request.POST.get('alumnos')
        if alumnos:
            fecha = datetime.now().strftime('%Y-%m-%d')
            Inscripcion.objects.create(centro_educativo=id_centro,ciclo_grado=id_grado,alumno_id=int(alumnos), Fecha_inscripcion=fecha)
            return redirect('educacion:cg_list_para_inscribir_alumnos', id_centro_educativo=id_centro.id)

    #rol de director
class ListarAlumnosDeCadaCentro(IsDirectorCentroMixin, generic.ListView):
    model = Alumno
    template_name = 'directorCentro/alumnos_list_por_centro_educativo.html'
    context_object_name = 'obj'

    def get_object(self):
        user = self.request.user
        return centro_educativo.objects.filter(c_educativo__personal__perfile = user.user_profile).first()

    def get_queryset(self):
        centro = self.get_object()
        if centro:
            return Alumno.objects.filter(estado_alumno=True, A_alumnos__centro_educativo_id=centro.id)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['id_centro_educativo'] =  self.get_object()
        return context

class ListarGradosParaInscribirAlumnosDeCadaCentro(IsDirectorCentroMixin, generic.ListView):
    model = Ciclo_grado
    template_name = 'directorCentro/cg_list_para_inscribir_alumnos.html'
    context_object_name = 'obj'
    login_url = 'app:login'


    def get_queryset(self):
        # existe_ciclo = Ciclo.objects.filter(estado_ciclo=True, anio = datetime.now().year).first()
        # if existe_ciclo:
        #     return Ciclo_grado.objects.filter(estado_cg=True, ciclo=existe_ciclo).order_by('ciclo', 'seccion')
        # return None
        return Ciclo_grado.objects.filter(estado_cg=True).order_by('ciclo', 'seccion')

    def get_object(self):
        user = self.request.user
        return centro_educativo.objects.filter(c_educativo__personal__perfile = user.user_profile).first()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context['id_centro_educativo'] =  self.get_object()
        return context

class InscribirAlumnosPorCadaCentro(IsDirectorCentroMixin, generic.CreateView):
    model = Inscripcion
    template_name = 'directorCentro/alumnoInscripcionPorGrado.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_centro_educativo(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        if id_centro_educativo:
            return centro_educativo.objects.filter(id=int(id_centro_educativo)).first()
        return None

    def get_grado(self):
        id_grado = self.kwargs.get('id_grado')
        if id_grado:
            return Ciclo_grado.objects.filter(id=int(id_grado)).first()
        return None

    def get(self, request, *args, **kwargs):
        id_centro = self.get_centro_educativo()
        id_grado = self.get_grado()
        context={}
        context['id_centro_educativo'] =  id_centro
        context['id_grado'] = id_grado

        context['alumnos'] = Alumno.objects.filter(estado_alumno=True).exclude(id__in=Inscripcion.objects.filter(ciclo_grado__ciclo__anio=datetime.now().year).values_list('alumno_id'))
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id_centro = self.get_centro_educativo()
        id_grado = self.get_grado()
        alumnos = self.request.POST.get('alumnos')
        if alumnos:
            fecha = datetime.now().strftime('%Y-%m-%d')
            Inscripcion.objects.create(centro_educativo=id_centro,ciclo_grado=id_grado,alumno_id=int(alumnos), Fecha_inscripcion=fecha)
            return redirect('educacion:cg_list_para_inscribir_alumnos_por_cada_centro')
