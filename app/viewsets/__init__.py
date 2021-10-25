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
from .educacionViewset.personalViewset import PersonalView, PersonalNew, PersonalEdit, PersonalDel, ListarPersonalEducativoPorCentroEducativo
from .educacionViewset.religionViewset import ReligionView, ReligionNew, ReligionEdit, ReligionDel
from .educacionViewset.tareaViewset import TareaView, TareaNew, TareaEdit, TareaDel
from .educacionViewset.gradoViewset import GradoView, GradoNew, GradoEdit, GradoDel
from .educacionViewset.religionalumViewset import Religion_alumnoView, Religion_alumnoNew, Religion_alumnoEdit, Religion_alumnoDel
from .educacionViewset.techoViewset import TechoView, TechoNew, TechoEdit, TechoDel
from .educacionViewset.paredViewset import ParedView, ParedNew, ParedEdit, ParedDel
from .educacionViewset.etniaViewset import EtniaView, EtniaNew, EtniaEdit, EtniaDel
from .educacionViewset.serviaguaViewset import ServiaguaView, ServiaguaNew, ServiaguaEdit, ServiaguaDel
from .educacionViewset.convivienteViewset import ConvivienteView, ConvivienteNew, ConvivienteEdit, ConvivienteDel, ConvivienteAlumnoEdit
from .educacionViewset.tutorViewset import TutorView, TutorNew, TutorEdit, TutorDel
from .educacionViewset.alumnoViewset import (AlumnoView, AlumnoNew, AlumnoEdit, AlumnoDel,
                                    AlumnoDetail, AlumnoDetailAndCreate,
                                    AlumnoEditViviendaConvivientes
                                    )
from .educacionViewset.centperViewset import CentPerView, CentPerNew, CentPerEdit, CentPerDel, AsignarPersonalEducativoCentroPersona
from .educacionViewset.estantViewset import EstAntView, EstAntNew, EstAntEdit, EstAntDel
from .educacionViewset.cgViewset import CGView, CGNew, CGEdit, CGDel, CiclosForCreateGradeandCourseView, CG_Del_Alumno
from .educacionViewset.cgcViewset import (CGCView, CGCNew, CGCEdit, CGCDel,
                                    Listar_Por_Centro_educativo_y_Por_Grado,
                                    Listar_cursos_y_Grados_Por_Personal_y_Centro_Educativo,
                                    Agregar_cursos_por_personal,
                                    CGDelAlumno)
from .educacionViewset.insViewset import (InsView, InsNew, InsEdit, InsDel,
                                ListarAlumnosPorCentroEducativo,
                                ListarGradosParaInscribirAlumnos,
                                InscribirAlumnos)
from .educacionViewset.viviendaViewset import VivView, VivNew, VivEdit, VivDel
from .educacionViewset.educacionViewset import HomeEducacion
from .educacionViewset.Reportes import (AlumnosPorEdad, AlumnosPorOcupacion, CantidadAlumnosPorCentro,
                                        CantidadAlumnosPorGenero, ReportesAlumnos)

#Municipalizacion
from .MunicViewset.municipalizacionViewset import HomeMunicipalizacion
from .MunicViewset.areaViewset import AreaView, AreaNew, AreaEdit, AreaDel
from .MunicViewset.curgradViewset import CarGView, CarGNew, CarGEdit, CarGDel
from .MunicViewset.idperViewset import IdPerView, IdPerNew, IdPerEdit, IdPerDel
from .MunicViewset.personaViewset import PerView, PerNew, PerEdit, PerDel
from .MunicViewset.benefViewset import BenView, BenNew, BenEdit, BenDel
from .MunicViewset.maestroViewset import MaesView, MaesNew, MaesEdit, MaesDel
from .MunicViewset.ProfesionViewset import ProfView, ProfNew, ProfEdit, ProfDel
from .MunicViewset.discViewset import DiscView, DiscNew, DiscEdit, DiscDel
from .MunicViewset.cargoViewset import CarView, CarNew, CarEdit, CarDel
from .MunicViewset.comisionViewset import ComView, ComNew, ComEdit, ComDel
from .MunicViewset.ausbenefiViewset import AusenBeneficiadoView, AusenBeneficiadoNew, AusenBeneficiadoEdit, AusenBeneficiadoDel
from .MunicViewset.establecimientoViewset import EstablecimientoView, EstablecimientoNew, EstablecimientoEdit, EstablecimientoDel
from .MunicViewset.lidercomuniViewset import LiderComunitarioMuniView, LiderComunitarioNew, LiderComunitarioEdit, LiderComunitarioDel
from .MunicViewset.mediocomuViewset import MedioComuniView, MedioComuniNew, MedioComuniEdit, MedioComuniDel
from .MunicViewset.partidopoliticViewset import PartidoPoliticView, PartidoPoliticNew, PartidoPoliticEdit, PartidoPoliticDel
from .MunicViewset.tutormuniViewset import TutorMuniView, TutorMuniNew, TutorMuniEdit, TutorMuniDel
from .MunicViewset.padperViewset import PadPerView, PadPerNew, PadPerEdit, PadPerDel
from .MunicViewset.padfamViewset import PadFamView, PadFamNew, PadFamEdit, PadFamDel
from .MunicViewset.benefarViewset import BenefArView, BenefArNew, BenefArEdit, BenefArDel
from .MunicViewset.ausenciaViewset import AusView, AusNew, AusEdit, AusDel
from .MunicViewset.idioma_MuniView import IdiomaMuniView, IdiomaMuniNew, IdiomaMuniEdit, IdiomaMuniDel
from .MunicViewset.MuniView import MunicView, MuniNew, MuniEdit, MuniDel
from .MunicViewset.DepView import DeptoView, DeptoNew, DeptoEdit, DeptoDel
from .MunicViewset.EtniaMuniView import EtnMuniView, EtniaMuniNew, EtniaMuniEdit, EtniaMuniDel
from .MunicViewset.estantMuniView import EstMuniView, EstMuniNew, EstMuniEdit, EstMuniDel
from .MunicViewset.PadecMuniView import PadMuniView, PadMuniNew, PadMuniEdit, PadMuniDel
from .MunicViewset.generoMuniView import GeneroMuniView, GeneroMuniNew, GeneroMuniEdit, GeneroMuniDel
from .MunicViewset.ocupMuniView import OcupacionMuniView, OcupacionMuniNew, OcupacionMuniEdit, OcupacionMuniDel
from .MunicViewset.corpmuniviewet import CorpMuniView, CorpMuniNew, CorpMuniEdit, CorpMuniDel
from .MunicViewset.goView import GrupoOrganizadoView, GrupoOrganizadoNew, GrupoOrganizadoEdit, GrupoOrganizadoDel
from .MunicViewset.programasView import ProgramasView, ProgramasNew, ProgramasEdit, ProgramasDel
from .MunicViewset.comisionNAView import ComisionNAView, ComisionNANew, ComisionNAEdit, ComisionNADel

#SocioProductivo
from .sociopViewset.HomeSocioproductivo import HomeSocioproductivo
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
from .sociopViewset.personabasicaView import PersonaBasicaView, PersonaBasicaNew, PersonaBasicaEdit, PersonaBasicaDel
from .sociopViewset.viviSoView import ViviendSoView, ViviendSoNew, ViviendSoEdit, ViviendSoDel
from .sociopViewset.encargadoView import EncargadoView, EncargadoNew, EncargadoEdit, EncargadoDel
from .sociopViewset.empreView import EmprenView, EmprenNew, EmprenEdit, EmprenDel
