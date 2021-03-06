from .educacionViewset.departamentoViewset import DepartamentoView, DepartamentoNew, DepartamentoEdit, DepartamentoDel
from .educacionViewset.municipioViewset import MunicipioView, MunicipioNew, MunicipioEdit, MunicipioDel
from .educacionViewset.parentescoViewset import ParentescoView, ParentescoNew, ParentescoEdit, ParentescoDel
from .educacionViewset.seccionviewset import SeccionView, SeccionNew, SeccionEdit, SeccionDel
from .educacionViewset.psicoViewset import PicoView, PsicoNew, PsicoEdit, PsicoDel
from .educacionViewset.catViewset import CatView, CatNew, CatEdit, CatDel
from .educacionViewset.tpisoViewset import TpisoView, TpisoNew, TpisoEdit, TpisoDel
from .educacionViewset.ocupViewset import OcupView, OcupNew, OcupEdit, OcupDel
from .educacionViewset.padViewset import PadView, PadNew, PadEdit, PadDel
from .educacionViewset.AlumPadViewset import APadView, APadNew, APadEdit, APadDel
from .educacionViewset.CenEduViewset import CenEdView, CenEdNew, CenEdEdit, CenEdDel
from .educacionViewset.homeViewset import Home
from .educacionViewset.cicloViewset import CicloView, CicloNew, CicloEdit, CicloDel
from .educacionViewset.cursoViewset import CursoView, CursoNew, CursoEdit, CursoDel
from .educacionViewset.generoViewset import GeneroView, GeneroNew, GeneroEdit, GeneroDel
from .educacionViewset.gradosViewset import GradosView, GradosNew, GradosEdit, GradosDel, ListarGradosPorCentroEducacion
from .educacionViewset.idiomaViewset import IdiomaView, IdiomaNew, IdiomaEdit, IdiomaDel
from .educacionViewset.personalViewset import (PersonalView, PersonalNew, PersonalEdit, PersonalDel,
                                                ListarPersonalEducativoPorCentroEducativo,
                                                PersonalDirectorCentroNew,
                                                PersonalMaestroNew,
                                                ListarPersonalEnCadaCentro)
from .educacionViewset.religionViewset import ReligionView, ReligionNew, ReligionEdit, ReligionDel
from .educacionViewset.gradoViewset import GradoView, GradoNew, GradoEdit, GradoDel
from .educacionViewset.religionalumViewset import Religion_alumnoView, Religion_alumnoNew, Religion_alumnoEdit, Religion_alumnoDel
from .educacionViewset.techoViewset import TechoView, TechoNew, TechoEdit, TechoDel
from .educacionViewset.paredViewset import ParedView, ParedNew, ParedEdit, ParedDel
from .educacionViewset.etniaViewset import EtniaView, EtniaNew, EtniaEdit, EtniaDel
from .educacionViewset.serviaguaViewset import ServiaguaView, ServiaguaNew, ServiaguaEdit, ServiaguaDel
from .educacionViewset.convivienteViewset import ConvivienteView, ConvivienteNew, ConvivienteEdit, ConvivienteDel, ConvivienteAlumnoEdit
from .educacionViewset.tutorViewset import TutorView, TutorNew, TutorEdit, TutorDel
from .educacionViewset.alumnoViewset import (AlumnoView, AlumnoNew, AlumnoEdit, AlumnoDel,
                                    AlumnoDetail, AlumnoDetailAndCreate, AlumnoDetailAndupdate, AlumnoupdateViviendaConvivientes,
                                    AlumnoEditViviendaConvivientes,
                                    AlumnosDeCadaCurso
                                    )
from .educacionViewset.centperViewset import (CentPerView, CentPerNew, CentPerEdit, CentPerDel,
                                    AsignarPersonalEducativoCentroPersona,
                                    AsignarDirectorACentroEducativo,
                                    ListarDirectoresPorCentroEducativo,
                                    ListarCentroEducativoPorMaestro)
from .educacionViewset.estantViewset import EstAntView, EstAntNew, EstAntEdit, EstAntDel
from .educacionViewset.cgViewset import (CGView, CGNew, CGEdit, CGDel,
                                    CiclosForCreateGradeandCourseView,
                                    CG_Del_Alumno)
from .educacionViewset.cgcViewset import (CGCView, CGCNew, CGCEdit, CGCDel,
                                    Listar_Por_Centro_educativo_y_Por_Grado,
                                    Listar_cursos_y_Grados_Por_Personal_y_Centro_Educativo,
                                    Agregar_cursos_por_personal,
                                    CGDelAlumno,
                                    Listar_cursos_del_personal_de_cada_centro,
                                    Asignar_curso_maestro_Rol_Director,
                                    Listar_cursos_por_maestro
                                    )
from .educacionViewset.insViewset import (InsView, InsNew, InsEdit, InsDel,
                                ListarAlumnosPorCentroEducativo,
                                ListarGradosParaInscribirAlumnos,
                                InscribirAlumnos,
                                ListarGradosParaInscribirAlumnosDeCadaCentro,
                                InscribirAlumnosPorCadaCentro,
                                ListarAlumnosDeCadaCentro)
from .educacionViewset.viviendaViewset import VivView, VivNew, VivEdit, VivDel
from .educacionViewset.educacionViewset import HomeEducacion
from .educacionViewset.Reportes import (AlumnosPorEdad, AlumnosPorOcupacion, CantidadAlumnosPorCentro,
                                        CantidadAlumnosPorGenero, ReportesAlumnos)
from .educacionViewset.reportes_pdf import  ReportesAlumnospdf
from .educacionViewset.etapaView import EtapaView, EtapaNew, EtapaEdit, EtapaDel
from .educacionViewset.ceView import CEView, CENew, Etapas_Del_Alumno
from .educacionViewset.inscripcionesViewSet import ListarAlumnosParaCentro, ListarEtapasParaInscribirAlumnos, EtapasInscribirAlumnos, InsEtapaDel
from .educacionViewset.reportes_general import ReportesAlumnosGeneral
#homes de usuarios
from .users.directorGeneral.HomeDirectorGeneral import HomeDirectorGeneral
from .users.CoordinadorEducacion.HomeCoordinadorEduacion import HomeCoordinadorEducacion
from .users.directorCentro.HomeDirectorCentro import HomeDirectorCentro
from .users.maestro.HomeMaestro import HomeMaestro
from .users.EquipoTecMunicipal.HomeEquipoMunicipal import HomeEquipoMunicipal
from .users.CoordinadorSocioProductivo.HomeSocioproductivo import HomeCoordinadorSocioproductivo
from .users.EquipoSocioproductivo.HomeEquipoSocioproductivo import HomeEquipoSocioproductivo

#users roles
from .users.directorGeneral.User import (CrearCoordinador, ListarCoordinadores,
                                            CrearDirectorGeneral, DeleteUserGeneral)

from .users.CoordinadorEducacion.User import (CrearAsistenteMaestroDirectorCentro,
                                        ListarAsistentesMaestrosDirectorCentro, DeleteUserEducacion)

from .users.directorCentro.User import ( CrearMaestroDeCadaCentro)

from .users.mixins.CooEducacionDirectorCentroMaestro import RolesCooEducacionDirectorCentroMaestroMixin
from .users.mixins.CooEduacionDirectorCentro import RolesCooEducacionDirectorCentroMixin
from .users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin

from .users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from .users.CoordinadorMunicipal.User import CrearEquipoMunicipalYAsistenteMunicipal,ListarPersonalEquipoMunicipalAsistenteMunicipal, DeleteUserMuni

from .users.CoordinadorSocioProductivo.User import CrearAsistenteSocioproductivoEquipoSocio, ListarAsistenteSocioproductivoEquipoSocio, DeleteUserSocio
from .users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from .users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

#login
from .users.viewsets.User import Login2

#Municipalizacion
from .MunicViewset.municipalizacionViewset import HomeMunicipalizacion
from .MunicViewset.areaViewset import AreaView, AreaNew, AreaEdit, AreaDel
from .MunicViewset.curgradViewset import CarGView, CarGNew, CarGEdit, CarGDel
from .MunicViewset.idperViewset import IdPerView, IdPerNew, IdPerEdit, IdPerDel
from .MunicViewset.personaViewset import PerView, PerNew, PerEdit, PerDel
from .MunicViewset.benefViewset import BenView, BenNew, BenEdit, BenDel, BenDetail, ListarPorArea
from .MunicViewset.maestroViewset import MaesView, MaesNew, MaesEdit, MaesDel, MaesDetail
from .MunicViewset.ProfesionViewset import ProfView, ProfNew, ProfEdit, ProfDel
from .MunicViewset.cargoViewset import CarView, CarNew, CarEdit, CarDel
from .MunicViewset.tmedioViewset import TmedioView, TmedioNew, TmedioEdit, TmedioDel
from .MunicViewset.comisionViewset import ComView, ComNew, ComEdit, ComDel
from .MunicViewset.establecimientoViewset import EstablecimientoView, EstablecimientoNew, EstablecimientoEdit, EstablecimientoDel
from .MunicViewset.lidercomuniViewset import LiderComunitarioMuniView, LiderComunitarioNew, LiderComunitarioEdit, LiderComunitarioDel, LiderComunitarioDetail
from .MunicViewset.mediocomuViewset import MedioComuniView, MedioComuniNew, MedioComuniEdit, MedioComuniDel, MedioComuniDetail
from .MunicViewset.partidopoliticViewset import PartidoPoliticView, PartidoPoliticNew, PartidoPoliticEdit, PartidoPoliticDel
from .MunicViewset.tutormuniViewset import TutorMuniView, TutorMuniNew, TutorMuniEdit, TutorMuniDel
from .MunicViewset.padfamViewset import PadFamView, PadFamNew, PadFamEdit, PadFamDel,PadFamDetail
from .MunicViewset.benefarViewset import BenefArView, BenefArNew, BenefArEdit, BenefArDel, Area_beneficiado, BenefArListGeneral
from .MunicViewset.idioma_MuniView import IdiomaMuniView, IdiomaMuniNew, IdiomaMuniEdit, IdiomaMuniDel
from .MunicViewset.MuniView import MunicView, MuniNew, MuniEdit, MuniDel
from .MunicViewset.DepView import DeptoView, DeptoNew, DeptoEdit, DeptoDel
from .MunicViewset.EtniaMuniView import EtnMuniView, EtniaMuniNew, EtniaMuniEdit, EtniaMuniDel
from .MunicViewset.estantMuniView import EstMuniView, EstMuniNew, EstMuniEdit, EstMuniDel
from .MunicViewset.generoMuniView import GeneroMuniView, GeneroMuniNew, GeneroMuniEdit, GeneroMuniDel
from .MunicViewset.ocupMuniView import OcupacionMuniView, OcupacionMuniNew, OcupacionMuniEdit, OcupacionMuniDel
from .MunicViewset.corpmuniviewet import CorpMuniView, CorpMuniNew, CorpMuniEdit, CorpMuniDel, CorpMuniDetail
from .MunicViewset.goView import GrupoOrganizadoView, GrupoOrganizadoNew, GrupoOrganizadoEdit, GrupoOrganizadoDel
from .MunicViewset.programasView import ProgramasView, ProgramasNew, ProgramasEdit, ProgramasDel
from .MunicViewset.comisionNAView import ComisionNAView, ComisionNANew, ComisionNAEdit, ComisionNADel, ComisionNADetail
from .MunicViewset.reportes_muni import AlumnosporDepto, total_comisiones, total_corporaciones, total_maestros, Total_lideres, Total_medios, Total_padres
from .MunicViewset.gradoacadView import GradoacadView, GradoacadNew, GradoacadEdit, GradoacadDel
from .MunicViewset.reportemuniViewset import AlumnosporDeptosView, ListAlumnosDeptoPdf, total_corporacionesPDF, total_comisionesPDF, Total_lideresPDF, total_maestrosPDF, Total_mediosPDF, Total_padresPDF
from .MunicViewset.tpisomuniView import Tpiso_muniView, Tpiso_muniNew, Tpiso_muniEdit, Tpiso_muniDel
from .MunicViewset.techomuniView import TechomuniView, TechomuniNew, TechomuniEdit, TechomuniDel
from .MunicViewset.tparedmuniView import ParedmuniView, ParedmuniNew, ParedmuniEdit, ParedmuniDel
from .MunicViewset.categoriamuniview import CatmuniView, CatmuniNew, CatmuniEdit, CatmuniDel
#SocioProductivo
from .sociopViewset.aspectos_saludView import (AspectosSaludNew, AspectosSaludEdit, AspectosSaludDel,
                                            AspectosSaludView)
from .sociopViewset.tipo_EmpView import TipoEmpView, TipoEmpNew, TipoEmpEdit, TipoEmpDel
from .sociopViewset.electView import ElectView, ElectNew, ElectEdit, ElectDel
from .sociopViewset.jornadaesView import JornadaEsView, JornadaEsNew, JornadaEsEdit, JornadaEsDel
from .sociopViewset.grupoNAView import GrupoNAView, GrupoNANew, GrupoNAEdit, GrupoNADel
from .sociopViewset.ocupTutorView import OcupTutorView,OcupTutorNew, OcupTutorEdit,OcupTutorDel
from .sociopViewset.gradoactView import GradoactView, GradoactNew, GradoactEdit, GradoactDel
from .sociopViewset.electVivView import ElectvivView, ElectvivNew, ElectvivEdit, ElectvivDel
from .sociopViewset.aspectos_saludView import AspectosSaludView, AspectosSaludNew, AspectosSaludEdit, AspectosSaludDel
from .sociopViewset.talleresView import TallerView, TallerNew, TallerEdit, TallerDel
from .sociopViewset.infoeducacionView import InfoEducacionView, InfoEducacionNew, InfoEducacionEdit, InfoEducacionDel
from .sociopViewset.personabasicaView import PersonaBasicaView, PersonaBasicaNew, PersonaBasicaEdit, PersonaBasicaDel, personabDetail, ListarParticipantesPorTaller, ListarParticipantesCertificados, ListarParticipantesParaEmprendimientos
from .sociopViewset.viviSoView import ViviendSoView, ViviendSoNew, ViviendSoEdit, ViviendSoDel
from .sociopViewset.encargadoView import EncargadoView, EncargadoNew, EncargadoEdit, EncargadoDel
from .sociopViewset.empreView import EmprenView, EmprenNew, EmprenEdit, EmprenDel
from .sociopViewset.inscp_view import InscpView, InscpNew, InscpEdit, InscpDel, InscribirParticipanteTaller
from .sociopViewset.formlabView import  FormLabNew, FormLabView, formlabEdit, formlabDelete
from .sociopViewset.reportes_sociop import ParticipantesSociop
from .sociopViewset.munisocioView import MunicSocioView, MunicSocioNew, MunicSocioEdit, MunicSocioDel
from .sociopViewset.depsocioView import DepsocioView, DepsocioNew, DepsocioEdit, DepsocioDel
from .sociopViewset.etniasocioView import EtnsocioView, EtnsocioNew, EtnsocioEdit, EtnsocioDel
from .sociopViewset.generosocioView import GenerosocioView, GenerosocioNew, GenerosocioEdit, GenerosocioDel
from .sociopViewset.pisosocioView import TpisosocioView, TpisosocioNew, TpisosocioEdit, TpisosocioDel
from .sociopViewset.techosocioView import TechosocioView, TechosocioNew, TechosocioEdit, TechosocioDel
from .sociopViewset.paredsocioView import ParedsocioView, ParedsocioNew, ParedsocioEdit, ParedsocioDel
from .sociopViewset.catsocioView import CatsocioView, CatsocioNew, CatsocioEdit, CatsocioDel
from .sociopViewset.parentescosocioView import ParentescosocioView, ParentescosocioNew, ParentescosocioEdit, ParentescosocioDel
from .sociopViewset.reportesocio_pdf import ParticipantesSociopdf
from .sociopViewset.repo_director import ParticipantesSociop_direc
#Reportes del director director general
from .MunicViewset.reportes_director_general import reporte_participantes, reporte_comisiones, reporte_corporaciones, reporte_maestros, reporte_lideres, reporte_medios, reporte_padres
