from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Inscripcion, Alumno, centro_educativo, Ciclo_grado
from app.forms import InsForm
from datetime import datetime

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
class ListarAlumnosPorCentroEducativo(LoginRequiredMixin, generic.ListView):
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

class ListarGradosParaInscribirAlumnos(LoginRequiredMixin, generic.ListView):
    model = Ciclo_grado
    template_name = 'educacion/cg_list_para_inscribir_alumnos.html'
    context_object_name = 'obj'
    login_url = 'app:login'
    queryset = Ciclo_grado.objects.order_by('ciclo', 'seccion')

    def get_object(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        if id_centro_educativo:
            return centro_educativo.objects.filter(id=int(id_centro_educativo)).first()
        return None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        context['id_centro_educativo'] =  self.get_object()
        return context

class InscribirAlumnos(LoginRequiredMixin, generic.CreateView):
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
        

    