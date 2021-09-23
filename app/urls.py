from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import  url
from app import viewsets

router = routers.DefaultRouter()
router.register(r'personalEducativo', viewsets.PersonalViewset)
router.register(r'alumno', viewsets.AlumnoViewset)
router.register(r'religion', viewsets.religionViewset)
router.register(r'alumnoPadecimiento', viewsets.AlPAViewset)
router.register(r'categoria', viewsets.CategoriaViewset)
router.register(r'centroPersona', viewsets.CentroPViewset)
router.register(r'centro', viewsets.CentroViewset)
router.register(r'cicloGradoCurso', viewsets.CgcViewset)
router.register(r'cicloGrado', viewsets.CgViewset)
router.register(r'caonviviente', viewsets.ConvivienteViewset)
router.register(r'curso', viewsets.CursoViewset)
router.register(r'departamento', viewsets.DepartamentoViewset)
router.register(r'estiosAnteriores',viewsets.estuantoViewset)
router.register(r'etnia', viewsets.EtniaViewset)
router.register(r'genero', viewsets.GeneroViewset)
router.register(r'grado', viewsets.GradoViewset)
router.register(r'grados', viewsets.GradosViewset)
router.register(r'idioma', viewsets.IdiomaViewset)
router.register(r'inscripcion', viewsets.InViewset)
router.register(r'municipio', viewsets.MuniViewset)
router.register(r'ocupacion', viewsets.OcupacionViewset)
router.register(r'padecimiento', viewsets.PadecimientoViewset)
router.register(r'parentesco', viewsets.ParentescoViewset)
router.register(r'psicologico', viewsets.psicologicoViewset)
router.register(r'religionAlumno', viewsets.Religion_alumnoViewset)
router.register(r'seccion', viewsets.SeccionViewset)
router.register(r'servicioAgua', viewsets.Servicio_aguaViewset)
router.register(r'tarea', viewsets.TareaViewset)
router.register(r'tareaAlumno', viewsets.TAViewset)
router.register(r'tipoMuro', viewsets.Tipo_muroViewset)
router.register(r'tipoTecho', viewsets.Tipo_techoViewset)
router.register(r'tipoPiso', viewsets.TpisoViewset)
router.register(r'tutor', viewsets.TutorViewset)
router.register(r'vivienda', viewsets.ViviendaViewset)
urlpatterns = [
    path('app/',include(router.urls)),
    url(r"^app/token",obtain_auth_token, name="app-token"),
    path('api-auth/',include('rest_framework.urls')),
    ]
