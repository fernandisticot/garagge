from django.db import models
import datetime
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)

class Auto(models.Model):
	marca=models.CharField(max_length=30)
	modelo=models.CharField(max_length=30)
	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Trabajo(models.Model):
	fecha_inicio=models.DateField()
	terminado=models.BooleanField(default=False)
	auto=models.ForeignKey(Auto, on_delete=models.CASCADE)

class Horas(models.Model):
	cantidad=models.IntegerField(default=0)
	precio=models.IntegerField(default=0)
	fecha=models.DateField(default=datetime.date.today )
	trabajo=models.ForeignKey(Trabajo, on_delete=models.CASCADE)
	
class Depositos(models.Model):
	fecha=models.DateField(default=datetime.date.today)
	monto=models.IntegerField()
	trabajo=models.ForeignKey(Trabajo, on_delete=models.CASCADE)

class Piezas_usadas(models.Model):
	numero_de_serie=models.CharField(max_length=30 , null=True)
	trabajo=models.ForeignKey(Trabajo, null=True, on_delete=models.CASCADE)
	precio=models.IntegerField(default=0)
	descripcion=models.CharField(max_length=30, default=" no hay descripcion")
	marca=models.CharField(max_length=30, default="000000")
	modelo=models.CharField(max_length=30, default="000000")
	cantidad=models.IntegerField(default=0)


#modelos que contiene las piezas disponibles al interior del inventario
class Piezas_en_inventario(models.Model):
	numero_de_serie=models.CharField(max_length=30, default="o00000o")
	marca=models.CharField(max_length=30, default="000000")
	modelo=models.CharField(max_length=30, default="000000")
	ubicacion=models.CharField(max_length=30, default="o00000o")
	precio=models.IntegerField(default=0)
	stock=models.IntegerField(default=0)
	descripcion=models.CharField(max_length=30, default=" no hay descripcion")
	image=models.ImageField(upload_to='media/', default='media/default.jpg')

class Usos(models.Model):
	usos=models.CharField(max_length=52)

	def _str_(self):
		return self.usos
	
class PiezaUso(models.Model):
	pieza=models.ForeignKey(Piezas_en_inventario, on_delete=models.CASCADE)
	uso=models.ForeignKey(Usos, on_delete=models.CASCADE)
	esutilizable=models.BooleanField(default=True)

class Ventas(models.Model):
	numero_de_serie=models.CharField(max_length=30 , null=True)
	descripcion=models.CharField(max_length=512)
	monto=models.IntegerField(default=0)
	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
	marca=models.CharField(max_length=30, default="000000")
	modelo=models.CharField(max_length=30, default="000000")
	cantidad=models.IntegerField(default=0)
	fecha=models.DateField(default=datetime.date.today)


