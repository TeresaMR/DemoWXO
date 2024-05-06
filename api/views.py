from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 

from .models import Trabajadores, Vacaciones, Fechas_Importantes
from .serializer import TrabajadorSerializer,VacacionesSerializer, TrabajadorDiasVacacionesSerializer, FechasImportantesSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TrabajadorSerializer,VacacionesSerializer,FechasImportantesSerializer, TrabajadorDiasVacacionesSerializer,FechasOpcionesSerializer
from django.http import Http404
from django import http 

from django.utils import timezone

from rest_framework.status import HTTP_204_NO_CONTENT

from django import db

from datetime import datetime, timedelta

#API FOR TRABAJADORES
@api_view(['GET']) 
def get_list_Trabajadores(request): 

    trabajadores = Trabajadores.objects.all() 
    serializer = TrabajadorSerializer(trabajadores, many=True) 
    return Response(serializer.data) 

@api_view(['POST'])
def post_new_Trabajador(request):
	serializer = TrabajadorSerializer(data=request.data) 
	if serializer.is_valid(): 
		serializer.save() 
		return Response(serializer.data, status=status.HTTP_201_CREATED) 
	else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
	

@api_view(['GET']) 
def get_Trabajador(request, id): 
 return_trabajador=None
 try:
    trabajadores = Trabajadores.objects.all()
   # id=request.data
    for trabajador in trabajadores:
        print("en el for")
        if trabajador.id==id:
            print(trabajador.nombre)
            return_trabajador=trabajador
            
            if return_trabajador is not None:
                serializer=TrabajadorSerializer(return_trabajador)
                return Response(serializer.data)
            else:
                
                trabajador0=Trabajadores(0,"persona","ejemplo",0)
                serializer=TrabajadorSerializer(trabajador0)
                return serializer
 except Trabajadores.DoesNotExist:
            raise http.HttpResponseForbidden
 

@api_view(['GET'])
def get_dias_Vacaciones_Trabajador(request, id):
    return_trabajador=None
    try:
        trabajadores = Trabajadores.objects.all()
        for trabajador in trabajadores:
               # id=request.data
                if trabajador.id==id:
                    #print(trabajador.nombre)
                    return_trabajador=trabajador
                    
                if return_trabajador is not None:
                       serializer=TrabajadorDiasVacacionesSerializer(return_trabajador)
                       return Response(serializer.data)
                
        if return_trabajador is None:
            trabajador0=Trabajadores(0,"persona","ejemplo",0)
            serializer=TrabajadorDiasVacacionesSerializer(trabajador0)
            return Response(serializer.data)
        
    except Trabajadores.DoesNotExist:
            raise http.HttpResponseForbidden
	

@api_view(['PUT'])
def update_dias_Vacaciones_Trabajador(request,id):
    try:
    
        trabajador = Trabajadores.objects.get(pk=id)

        serializer = TrabajadorDiasVacacionesSerializer(trabajador, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    except Trabajadores.DoesNotExist:
        return Response({'error': 'Trabajador not found'}, status=404)
    

#API VACACIONES
@api_view(['GET']) 
def get_list_Future_Vacations(request):
    list_future_vacaciones=list()
    vacaciones=Vacaciones.objects.all()

    for vacacion in vacaciones:
         
         if vacacion.fechaInicio < timezone.now().date():
            serializer=VacacionesSerializer(vacacion)
            list_future_vacaciones.append(serializer)

        
    return Response(list_future_vacaciones)
     
    #GET VACACIONES AGENDADAS POR TRABAJADOR 
@api_view(['GET']) 
def get_Trabajador_Vacations(request, id):
    return_vacaciones=list()
    try:
        vacaciones = Vacaciones.objects.all()
        for vacacion in vacaciones:
                if vacacion.idTrabajador==id:
                    serializer=VacacionesSerializer(vacacion)
                    return_vacaciones.append(serializer)
        
        return Response(return_vacaciones)
    except Vacaciones.DoesNotExist:
            raise http.HttpResponseForbidden
     

@api_view(['POST'])
def post_Vacaciones(request):
    serializer = VacacionesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_Vacaciones_Status(id,request):
    try:
    
        if(request.data == False):
            #si la vacación no fue aprobada
            borrar_vacacion(id)
        elif request.data== True:
            vacaciones = Vacaciones.objects.get(pk=id)
            serializer = VacacionesSerializer(vacaciones, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

        
    except Vacaciones.DoesNotExist:
        return Response({'error': 'Vacaciones does not found'}, status=404)



   #serializer = VacacionesSerializer(vacaciones, data=request.data)

    """ if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        """ 

@api_view(['DELETE'])
def borrar_vacacion(id):
    try:
    
        vacaciones = Vacaciones.objects.get(pk=id)
        vacaciones.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        

    except Trabajadores.DoesNotExist:
        return Response({'error': 'Trabajador not found'}, status=404)
    

#CALCULAR FECHAS POSIBLES PARA VACACIONES
@api_view(['GET'])
def get_fechas_posibles(request,id,diasTomar):
   
    fecha_vacacion=dict() 
   
    fechas=Fechas_Importantes.objects.all() 
    fechas_posibles=list()
         
    serializer_fecha=FechasImportantesSerializer(fechas,many=True)
 
    cont = 1
    return_trabajador=None
    trabajadores = Trabajadores.objects.all()
    for trabajador in trabajadores:
            if trabajador.id==id:
                return_trabajador=trabajador
    

    diasVacaciones=return_trabajador.diasVacaciones
    if diasVacaciones>=0  and diasTomar<=diasVacaciones:
        
       
        for fechaNot in serializer_fecha.data:
            print(fechaNot)
            
            date_format = "%Y-%m-%d"  # Year-Month-Day format (YYYY-MM-DD)
            fechaInit=datetime.strptime(fechaNot['fechaFinal'],date_format)+timedelta(days=2)
            fechaFin=fechaInit+timedelta(days=diasTomar)

            fecha_vacacion={'fechaInicio':fechaInit.date(), 'fechaFinal':fechaFin.date()}
            #cont += 1
            fechas_posibles.append(fecha_vacacion)

        return Response(fechas_posibles)

    else:
        return Response("No tienes vacaciones suficientes")

     

#API FECHAS IMPORTANTES
@api_view(['GET']) 
def get_list_Future_FechasImportantes(request): 
    list_future_fechasImportantes=list()
    fechas_Importantes = Fechas_Importantes.objects.all() 
    for fecha in fechas_Importantes:
         if fecha.fechaInicio < timezone.now().date():
            
            list_future_fechasImportantes.append(fecha)

    serializer = FechasImportantesSerializer(list_future_fechasImportantes, many=True) 
    return Response(serializer.data) 

    #GET ALL FECHAS IMPORTANTES
@api_view(['GET']) 
def get_list_All_FechasImportantes(request): 

    fechas_Importantes = Fechas_Importantes.objects.all() 
    serializer = FechasImportantesSerializer(fechas_Importantes, many=True) 
    return Response(serializer.data) 

    #POST FECHAS IMPORTANTES 
@api_view(['POST'])
def post_new_FechaImportante(request):
    #print(request)
   # print(request.data)
    #print(request)
    serializer = FechasImportantesSerializer(data=request.data)
    print("holis")
    print(serializer)
    if serializer.is_valid(): 
        serializer.save() 
        print("en if")
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    else: 
         print("en else")
         print(serializer)
         #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def post_new_Fecha(request):
	serializer = FechasImportantesSerializer(data=request.data) 
	if serializer.is_valid(): 
		serializer.save() 
		return Response(serializer.data, status=status.HTTP_201_CREATED) 
	else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
	

     

def delete_all():
    try:
        Trabajadores.delete(Trabajadores.objects.all())
        Vacaciones.delete(Vacaciones.objects.all())
        Fechas_Importantes.delete(Fechas_Importantes.objects.all())

        print("Registros limpiados")
    except: print("Hubo un error al limpiar los regsitros")
     
     



