
from django.urls import path
#from .views import * 
from .views import update_dias_Vacaciones_Trabajador, get_Trabajador, get_dias_Vacaciones_Trabajador, get_list_Trabajadores, get_list_Future_Vacations,get_list_Future_FechasImportantes,get_list_All_FechasImportantes,post_new_FechaImportante, get_Trabajador_Vacations, update_Vacaciones_Status, borrar_vacacion,  post_new_Trabajador,post_new_Fecha, post_Vacaciones, get_fechas_posibles


app_name = 'api'

urlpatterns = [
    path('trabajadores/getAll', get_list_Trabajadores), 
    path('trabajador/<int:id>/getvacaciones', get_dias_Vacaciones_Trabajador),
    path('trabajador/get/<int:id>', get_Trabajador),
    path('trabajador/<int:id>/dias_vacaciones/update', update_dias_Vacaciones_Trabajador),
    path('trabajador/new', post_new_Trabajador),

    path('vacaciones/getfuture/alltrabajadores', get_list_Future_Vacations),
    path('vacaciones/trabajador/get/shedule/vacaciones/<int:id>',get_Trabajador_Vacations),
    path('vacaciones/update/status/<int:id>', update_Vacaciones_Status),
    path('vacaciones/borrar/<int:id>', borrar_vacacion),
    path('vacaciones/new', post_Vacaciones),
    path('vacaciones/getOpciones/<int:id>/<int:diasTomar>',get_fechas_posibles),

    path('fechasImportante/getFuture', get_list_Future_FechasImportantes),
    path('fechasImportantes/getAll',get_list_All_FechasImportantes),
    path('fechasImportantes/new',post_new_Fecha)

]