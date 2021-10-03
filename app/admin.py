from django.contrib import admin
from .models.educacion_model.ocupacion import ocupacion
from .models.educacion_model.religion import religion
from .models.educacion_model.grados import grados
from .models.educacion_model.genero import genero
from .models.educacion_model.tarea import tarea
from .models.educacion_model.personalEducativo import personalEducativo
from .models.educacion_model.tarea_alumno import tarea_alumno
from .models.educacion_model.vivienda import vivienda
from .models.educacion_model.departamento import departamento
from .models.educacion_model.centro_educativo import centro_educativo
from .models.educacion_model.idioma import idioma
from .models.educacion_model.conviviente import Conviviente
from .models.educacion_model.parentesco import Parentesco
from .models.educacion_model.servicio_agua import Servicio_Agua
from .models.educacion_model.alumnoModelo import Alumno
from .models.educacion_model.tipo_muro import Tipo_muro
from .models.educacion_model.tipo_techo import Tipo_techo
from .models.educacion_model.psicologicoModelo import psicologico
from .models.educacion_model.seccionModelo import seccion
from .models.educacion_model.categoriaModel import Categoria
from .models.educacion_model.tipopisoModel import Tipo_piso
from .models.educacion_model.centropersonaModel import Centropersona
from .models.educacion_model.estudiosantModel import EstudiosAnt
from .models.educacion_model.municipioModel import municipio
from .models.educacion_model.religion_alumno import Religion_alumno
from .models.educacion_model.grado import Grado
from .models.educacion_model.ciclo import Ciclo
from .models.educacion_model.curso import Curso
from .models.educacion_model.ciclo_grado import Ciclo_grado
from .models.educacion_model.ciclo_grado_curso import Ciclo_grado_curso
from .models.educacion_model.tutor import Tutor
from .models.educacion_model.padecimientoModel import Padecimiento
from .models.educacion_model.alumnopadecimiento import Apadecimiento
from .models.educacion_model.inscipsionesModel  import Inscripcion
from .models.educacion_model.etnia import etnia
#Municipalizacion
from .models.municipalizacionModel.area import Area
from .models.municipalizacionModel.ausencia import Ausencia
from .models.municipalizacionModel.Gorganizado import GOrganizado
from .models.municipalizacionModel.institucion import Institucion
from .models.municipalizacionModel.programaC import ProgramaC
from .models.municipalizacionModel.tutor_muni import TutorMuni
from .models.municipalizacionModel.establecimiento import Establecimiento
from .models.municipalizacionModel.mediocomu import MedioComuni
from .models.municipalizacionModel.partidopolitic import PartidoPolitic
from .models.municipalizacionModel.lider_comunitario import LiderComunitario
from .models.municipalizacionModel.ausen_beneficiado import AusenBeneficiado
from .models.municipalizacionModel.beneficiado import Beneficiado
from .models.municipalizacionModel.cargo import Cargo
from .models.municipalizacionModel.CarGrup import CargoGrupo
from .models.municipalizacionModel.comision import Comision
from .models.municipalizacionModel.idioPer import IdiomaPersona
from .models.municipalizacionModel.maestro import Maestro
from .models.municipalizacionModel.padper import PadPer
from .models.municipalizacionModel.persona import Persona
from .models.municipalizacionModel.profesion import Profesion
from .models.municipalizacionModel.comisionNA import ComisionNA
from .models.municipalizacionModel.benefArea import BeneficiadoArea
from .models.municipalizacionModel.padresFamilia import PadresFamilia
from .models.municipalizacionModel.corporacionMuni import CorporacionMunicipal

admin.site.register(ocupacion)
admin.site.register(religion)
admin.site.register(grados)
admin.site.register(genero)
admin.site.register(tarea)
admin.site.register(personalEducativo)
admin.site.register(tarea_alumno)
admin.site.register(vivienda)
admin.site.register(departamento)
admin.site.register(centro_educativo)
admin.site.register(idioma)
admin.site.register(Conviviente)
admin.site.register(Parentesco)
admin.site.register(Servicio_Agua)
admin.site.register(Alumno)
admin.site.register(Tipo_muro)
admin.site.register(Tipo_techo)
admin.site.register(psicologico)
admin.site.register(seccion)
admin.site.register(Categoria)
admin.site.register(Tipo_piso)
admin.site.register(Centropersona)
admin.site.register(EstudiosAnt)
admin.site.register(municipio)
admin.site.register(Religion_alumno)
admin.site.register(Grado)
admin.site.register(Ciclo)
admin.site.register(Curso)
admin.site.register(Ciclo_grado)
admin.site.register(Ciclo_grado_curso)
admin.site.register(Tutor)
admin.site.register(Padecimiento)
admin.site.register(Apadecimiento)
admin.site.register(Inscripcion)
admin.site.register(etnia)
#municipalizacion
admin.site.register(Area)
admin.site.register(Ausencia)
admin.site.register(GOrganizado)
admin.site.register(Institucion)
admin.site.register(ProgramaC)
admin.site.register(TutorMuni)
admin.site.register(Establecimiento)
admin.site.register(MedioComuni)
admin.site.register(PartidoPolitic)
admin.site.register(LiderComunitario)
admin.site.register(AusenBeneficiado)
admin.site.register(Beneficiado)
admin.site.register(Cargo)
admin.site.register(CargoGrupo)
admin.site.register(Comision)
admin.site.register(IdiomaPersona)
admin.site.register(Maestro)
admin.site.register(PadPer)
admin.site.register(Persona)
admin.site.register(Profesion)
admin.site.register(ComisionNA)
admin.site.register(BeneficiadoArea)
admin.site.register(PadresFamilia)
admin.site.register(CorporacionMunicipal)
