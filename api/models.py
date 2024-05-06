from django.db import models

# Create your models here.
#from django.db.models import TimeStampedModel, SoftDeletableModel
 

class Trabajadores(models.Model):
	id 				= models.AutoField(primary_key=True)
	nombre 				= models.TextField(max_length=5000, null=False, blank=True)
	apellido 		= models.TextField(max_length=5000, null=False, blank=True)
	diasVacaciones 		= models.IntegerField()
	
	def __str__(self):
		return self.title


class Vacaciones(models.Model):
	idVacaciones= models.AutoField(primary_key=True)
	fechaInicio= models.DateField(auto_now_add=False, verbose_name="fecha inicio vacaciones")
	fechaFinal= models.DateField(auto_now=False, verbose_name="fecha fin vacaciones")
	aprobado  =models.BooleanField()
	idTrabajador = models.ForeignKey(Trabajadores, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
	

class Fechas_Importantes(models.Model):
	idFecha 				= models.AutoField(primary_key=True)
	fechaInicio 			= models.DateField(auto_now_add=False, verbose_name="fecha inicio evento")
	fechaFinal 		= models.DateField(auto_now_add=False, verbose_name="fecha fin evento")
	nombreEvento 		= models.TextField(max_length=5000, null=False, blank=True)
	
	def __str__(self):
		return f"Fechas Importantes: {self.nombreEvento} (Inicio: {self.fechaInicio}, Fin: {self.fechaFinal})"
