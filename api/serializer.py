from .models import Trabajadores, Vacaciones, Fechas_Importantes
from rest_framework import serializers


class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabajadores
        fields = ['id', 'nombre', 'apellido', 'diasVacaciones']

class TrabajadorDiasVacacionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #####
        model = Trabajadores
        fields = ['diasVacaciones']

class VacacionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacaciones
        fields = ['idVacaciones','fechaInicio','fechaFinal']


class FechasImportantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fechas_Importantes
        fields = ['fechaInicio','fechaFinal','nombreEvento']

class FechasOpcionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fechas_Importantes
        fields = ['fechaInicio','fechaFinal']