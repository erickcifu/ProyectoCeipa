from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from app.forms.educacionForms.cgcForm import CGCFormCreateForPersonal

from app.models import Ciclo_grado_curso, Ciclo_grado, centro_educativo
from app.forms import CGCForm, CGCFormCreate
from django.db.models import F
from app.models.educacion_model.alumnoModelo import Alumno

from app.models.educacion_model.personalEducativo import personalEducativo

class CGCView(LoginRequiredMixin, generic.ListView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cgc_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_queryset(self):
        qs = Ciclo_grado_curso.objects.all()
        cg_id = self.request.GET.get("lang")
        if cg_id:
            qs = qs.filter(ciclo_grado__id=cg_id)
        return qs
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['id_grado_ciclo'] =  self.request.GET.get("lang") if self.request.GET.get("lang") else None
        return context

class CGCNew(LoginRequiredMixin, generic.CreateView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cgc_form.html'
    context_object_name = "obj"
    form_class = CGCFormCreate
    success_url = reverse_lazy("educacion:cgc_list")
    login_url = 'app:login'

    def get_queryset(self):
        return Ciclo_grado.objects.all()
        
    def get_object(self):
        id_ciclo_grado = self.kwargs.get('pk')
        qs = None
        if id_ciclo_grado:
            qs = self.get_queryset().filter(id=id_ciclo_grado).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_grado_ciclo'] = self.get_object()
        return context

    def form_valid(self, form):
        if form.is_valid():
            ciclo_grado = self.get_object()
            if ciclo_grado: 
                ciclo_grado_curso = Ciclo_grado_curso(**form.cleaned_data, ciclo_grado = ciclo_grado)
                print(ciclo_grado_curso.ciclo_grado, ciclo_grado_curso.curso)
                ciclo_grado_curso.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class CGCEdit(LoginRequiredMixin, generic.UpdateView):
    model = Ciclo_grado_curso
    template_name = "educacion/cgc_form_update.html"
    context_object_name = "obj"
    form_class = CGCForm
    success_url = reverse_lazy("educacion:cgc_list")
    login_url = 'app:login'

class CGCDel(LoginRequiredMixin, generic.DeleteView):
    model = Ciclo_grado_curso
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:cgc_list")


#Traer los cursos pertenecientes al grado de un ciclo y que pertenezcan a un centro educativo
class Listar_Por_Centro_educativo_y_Por_Grado(LoginRequiredMixin, generic.ListView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cursos_por_centro_educativo_y_grado.html'
    context_object_name = 'obj'

    def get_queryset(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        id_grado = self.kwargs.get('id_grado')
        if id_centro_educativo and id_grado:
            return Ciclo_grado_curso.objects.filter(ciclo_grado_id=int(id_grado)).filter(maestro__p_educativo__centro_Educativo__id=int(id_centro_educativo))

        #return None
    
    def get_centro_educativo(self, id):
        return centro_educativo.objects.filter(id=id).first()
    
    def get_grado(self, id):
        return Ciclo_grado.objects.filter(id=id).first()
    
    def get(self, request, *args, **kwargs):
        list = self.get_queryset()
        if list:
            context = {}
            context[str(self.context_object_name)] = list
            context['grado'] = self.get_grado(int(self.kwargs.get('id_grado')))
            context['centro_educativo'] = self.get_centro_educativo(int(self.kwargs.get('id_centro_educativo')))
            return render(request, self.template_name, context)
        else:
            return redirect('educacion:grados_por_centro_educacion')

#Ciclo_grado_curso.objects.filter(ciclo_grado_id=2).filter(maestro__p_educativo__centro_Educativo__id=1)

class Listar_cursos_y_Grados_Por_Personal_y_Centro_Educativo(LoginRequiredMixin, generic.ListView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cursos_por_grado_por_personal_y_centro_educativo.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_queryset(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        id_maestro = self.kwargs.get('id_maestro')
        if id_centro_educativo and id_maestro:
            return Ciclo_grado_curso.objects.filter(maestro_id=int(id_maestro)).filter(maestro__p_educativo__centro_Educativo__id=int(id_centro_educativo)).annotate(grado = F('ciclo_grado__grado__nombre_grado'), seccion = F('ciclo_grado__seccion__nombre_seccion'), ciclo = F('ciclo_grado__ciclo__anio'))
        return None
    
    def get_object(self):
        id_maestro = self.kwargs.get('id_maestro')
        if id_maestro:
            return personalEducativo.objects.filter(id=int(id_maestro)).first()
        return None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        print(type(self.get_object().id))
        context['personal'] =  self.get_object()
        context['id_centro_educativo'] =  centro_educativo.objects.filter(id=int(self.kwargs.get('id_centro_educativo'))).first()
        return context

class Agregar_cursos_por_personal(LoginRequiredMixin, generic.CreateView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cgc_por_maestro.html'
    context_object_name = "obj"
    form_class = CGCFormCreateForPersonal
    success_url = reverse_lazy("educacion:cgc_list")
    login_url = 'app:login'

    def get_queryset(self):
        return personalEducativo.objects.all()
        
    def get_object(self):
        id_maestro = self.kwargs.get('pk')
        qs = None
        if id_maestro:
            qs = self.get_queryset().filter(id=int(id_maestro)).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maestro'] = self.get_object()
        context['grado_ciclo'] = Ciclo_grado.objects.exclude(cgc_cg__maestro__id = self.get_object().id)
        return context

    def form_valid(self, form):
        if form.is_valid():
            maestro = self.get_object()
            ciclo_grado = self.request.POST.get('ciclo_grado')
            if maestro and ciclo_grado: 
                ciclo_grado_curso = Ciclo_grado_curso(**form.cleaned_data, maestro=maestro, ciclo_grado_id = int(ciclo_grado))
                ciclo_grado_curso.save()
                return redirect('educacion:listado_personal_por_centro_educativo')
            else:
                return self.render_to_response(self.get_context_data(form=form))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class CGDelAlumno(LoginRequiredMixin, generic.ListView):
    model = Ciclo_grado_curso
    template_name = 'educacion/cursos_alumnos_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_object(self):
        id_alumno = self.kwargs.get('pk')
        if id_alumno:
            return Alumno.objects.filter(id=id_alumno).first()

    def get_queryset(self):
        id_alumno = self.kwargs.get('pk')
        if id_alumno:
            return Ciclo_grado_curso.objects.filter(ciclo_grado__ciclo_grado__alumno_id = int(id_alumno))
        return None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['alumno'] =  self.get_object()
        return context
