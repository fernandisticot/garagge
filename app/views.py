from django.shortcuts import render
from .models import *
from django.contrib.auth import *

# Create your views here.
def index(request):
	return render(request, 'app/index.html')
def loginView(request):
	return render(request, 'app/login.html')
def logoutView(request):
	logout(request)
	return render(request,'app/index.html')
def auth(request):
	username= request.POST['username']
	password= request.POST['password']
	usuario= authenticate(username=username, password=password)
	login(request, usuario)
	return render(request, 'app/index.html')
def Catalogo(request):
	#username= "Jaime"
	#password="Acevedo123"
	#user=User.objects.create_user(username=username, password=password)
	contexto={}
	contexto['Piezas']=Piezas_en_inventario.objects.all()
	return render(request,'app/catalogo.html' ,contexto)
def added_trabajo(request):
	return render(request,'app/added_trabajo.html')
def added_pieza(request):
	return render(request, 'app/added_pieza.html')

def add_trabajo(request):
	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	marca = request.POST['marca']
	modelo = request.POST['modelo']
	fecha = request.POST['fecha_inicio']

	contexto = {"form" : "Trabajo creado con exito", "gracias":"Garagge Acevedo le desea un buen día" , "nombre":nombre ,
	"apellido":apellido, "marca":marca , 
	"modelo":modelo , "fecha":fecha}

	cliente= Cliente(nombre=nombre, apellido=apellido)
	cliente.save()
	auto=Auto(marca=marca, modelo=modelo, cliente=cliente)
	auto.save()
	trabajo=Trabajo(fecha_inicio=fecha, terminado=False, auto=auto)
	trabajo.save()
	
	
	return render(request, 'app/added_trabajo.html' , contexto)

def add_pieza(request):
	numero_de_serie = request.POST['numero_de_serie']
	descripcion = request.POST['descripcion']
	ubicacion=request.POST['ubicacion']
	marca=request.POST['marca']
	modelo=request.POST['modelo']
	precio=request.POST['precio']
	stock=request.POST['stock']
	imagen=request.FILES['imagen']
	usosa=request.POST.getlist('usosa')
	usosb=Usos.objects.all()
	##usoc={'31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47'}

	contexto ={"form": "Pieza añadida a inventario", "gracias":"Favor no olvide ubicar la pieza en lugar acordado" , 
	"numero_de_serie":numero_de_serie , "ubicacion":ubicacion, "precio":precio , "marca":marca , "modelo":modelo , "stock":stock, "descripcion":descripcion,"Usooo":usosa}


	pieza=Piezas_en_inventario(numero_de_serie=numero_de_serie, descripcion=descripcion, marca=marca, modelo=modelo, ubicacion=ubicacion, precio=precio, stock=stock, image=imagen)
	pieza.save()
	for valor in usosa:
		for value in usosb:
			if valor==value.usos: ##valor es un nombre, value es un object pero value.usos es un nombre
				utilizable=PiezaUso(pieza=pieza, uso=value)
				utilizable.save()
			##else: ##valor es un codigo, value es un codigo pero value.usos es un nombre
			##	utilizable=PiezaUso(pieza=pieza, uso=value, esutilizable=False)
			##	utilizable.save()


	return render(request, 'app/added_pieza.html' , contexto)

def nuevo_trabajo(request):
	return render(request, 'app/nuevo_trabajo.html')
def nueva_pieza(request):
	contexto={}
	contexto['USOS']=Usos.objects.all()
	return render(request, 'app/nueva_pieza.html', contexto)

#def lista_trabajos(request):
	#contexto={}
	#contexto['trabajos'] = Trabajo.objects.all()
	#return render(request, 'app/lista_trabajos.html', contexto)

def lista_piezas(request):
	contexto={}
	contexto['Filtrado']=PiezaUso.objects.filter(esutilizable=True)
	contexto['trabajos']=Trabajo.objects.all()
	return render(request, 'app/lista_piezas.html' ,contexto)

def usar_pieza(request):
	lepieza=request.POST['unapieza']
	Pieza=Piezas_en_inventario.objects.get(pk=lepieza)
	cantidadusada=request.POST['inputNumber']
	cantidadusada=int(cantidadusada)
	precio=Pieza.precio
	numero_de_serie=Pieza.numero_de_serie
	descripcion=Pieza.descripcion
	marca=Pieza.marca
	modelo=Pieza.modelo
	stock=int(Pieza.stock)
	letrabajo=request.POST['traba']
	trabajo=Trabajo.objects.get(pk=letrabajo)
	ubicacion=Pieza.ubicacion

	if trabajo.terminado==False and stock==cantidadusada:
		piezausada=Piezas_usadas(numero_de_serie=numero_de_serie , trabajo=trabajo, precio=precio, descripcion=descripcion , marca=marca , modelo=modelo, cantidad=cantidadusada)
		piezausada.save()
		Pieza.delete()
		contexto={"ubicacion":ubicacion, "trabajo":trabajo, "numero_de_serie":numero_de_serie , "precio":precio, "descripcion":descripcion , "marca":marca , "modelo":modelo }
		return render(request,'app/used_pieza.html', contexto)

	elif trabajo.terminado==False and cantidadusada<stock:
		piezausada=Piezas_usadas(numero_de_serie=numero_de_serie , trabajo=trabajo, precio=precio, descripcion=descripcion , marca=marca , modelo=modelo, cantidad=cantidadusada)
		piezausada.save()
		nuevostock=stock-cantidadusada
		Pieza.stock=nuevostock
		Pieza.save()
		contexto={"cantidad":cantidadusada ,"ubicacion":ubicacion, "trabajo":trabajo, "numero_de_serie":numero_de_serie , "precio":precio, "descripcion":descripcion , "marca":marca , "modelo":modelo }
		return render(request,'app/used_pieza.html', contexto)

	else:
		return render(request,'app/trabajo_terminado.html')
def vender_pieza(request):
	lepieza=request.POST['unapieza']
	Pieza=Piezas_en_inventario.objects.get(pk=lepieza)
	cantidadusada=request.POST['inputNumber']
	cantidadusada=int(cantidadusada)
	monto=int(Pieza.precio)*cantidadusada
	numero_de_serie=Pieza.numero_de_serie
	descripcion=Pieza.descripcion
	marca=Pieza.marca
	modelo=Pieza.modelo
	stock=int(Pieza.stock)
	ubicacion=Pieza.ubicacion
	nombre=request.POST['nombre']
	apellido=request.POST['apellido']
	cliente=Cliente(nombre=nombre, apellido=apellido)
	cliente.save()
	if  stock==cantidadusada:
		venta=Ventas(cliente=cliente, numero_de_serie=numero_de_serie , monto=monto, descripcion=descripcion , marca=marca , modelo=modelo, cantidad=cantidadusada)
		venta.save()
		Pieza.delete()
		contexto={"ubicacion":ubicacion, "numero_de_serie":numero_de_serie , "monto":monto, "descripcion":descripcion , "marca":marca , "modelo":modelo }
		return render(request,'app/used_pieza.html', contexto)

	elif  cantidadusada<stock:
		venta=Ventas(cliente=cliente, numero_de_serie=numero_de_serie, monto=monto, descripcion=descripcion , marca=marca , modelo=modelo, cantidad=cantidadusada)
		venta.save()
		nuevostock=stock-cantidadusada
		Pieza.stock=nuevostock
		Pieza.save()
		contexto={"cantidad":cantidadusada ,"ubicacion":ubicacion, "numero_de_serie":numero_de_serie , "precio":precio, "descripcion":descripcion , "marca":marca , "modelo":modelo }
		return render(request,'app/used_pieza.html', contexto)
	else:
		return render(request,'app/index.html')


def used_pieza(request):
	return render(request,'app/used_pieza.html')
def trabajo_terminado(request):
	return render(request,'app/trabajo_terminado.html')
def terminar_trabajo(request):
	letrabajo=request.POST['traba']
	trabajo=Trabajo.objects.get(pk=letrabajo)
	trabajo.terminado=True
	trabajo.save()
	return render(request,'app/trabajo_terminado.html')
def elsubtotal(request):
	letrabajo=request.POST['id']
	mitrabajo=Trabajo.objects.get(pk=letrabajo)
	depositosatrabajo=Depositos.objects.filter(trabajo=mitrabajo)
	horas=Horas.objects.filter(trabajo=mitrabajo)
	total=[]
	for valor in Piezas_usadas.objects.filter(trabajo=mitrabajo):
		total.append(int(valor.precio)*int(valor.cantidad))
	for val in horas:
		total.append(int(val.cantidad)*int(val.precio))
	supertotal=0
	for i in total:
		supertotal=supertotal+i
	IVA=int(supertotal*0.19)
	megatotal=int(IVA+supertotal)
	pagos=[]
	for value in depositosatrabajo:
		pagos.append(int(value.monto)*-1)
	pagado=0
	for j in pagos:
		pagado=pagado+j
	adeudado=megatotal+pagado

	contexto={}
	contexto['piezasacobrar']=Piezas_usadas.objects.filter(trabajo=mitrabajo)
	contexto['depositosatrabajo']=depositosatrabajo
	contexto['horas']=horas
	contexto['mitrabajo']=mitrabajo
	contexto['supertotal']=supertotal
	contexto['IVA']=IVA
	contexto['megatotal']=megatotal
	contexto['adeudado']=adeudado
	return render(request,'app/subtotal.html',contexto)
def subtotal(request):
	return render(request, 'app/subtotal.html')
def sumar_horas(request):
	horasasumar=request.POST['horas']
	horasasumar=int(horasasumar)
	precio_hora=request.POST['precio_hora']
	precio_hora=int(precio_hora)
	trabajoaeditar=request.POST['id']
	trabajo=Trabajo.objects.get(pk=trabajoaeditar)
	if trabajo.terminado==False:
		hora=Horas(cantidad=horasasumar, precio=precio_hora, trabajo=trabajo)
		hora.save()
		return render(request,'app/index.html')
	else:
		return render(request,'app/trabajo_terminado.html')
def abonar(request):
	montoabonar=request.POST['monto']
	montoabonar=int(montoabonar)
	trabajoaeditar=request.POST['id']
	trabajoo=Trabajo.objects.get(pk=trabajoaeditar)
	abono=Depositos(monto=montoabonar,trabajo=trabajoo)
	abono.save()
	return render(request, 'app/index.html')
def abonos_y_subtotales(request):
	contexto={}
	contexto['trabajos']=Trabajo.objects.all()
	return render(request, 'app/abonos_y_subtotales.html', contexto)
def add_horas(request):
	contexto={}
	contexto['trabajos']=Trabajo.objects.all()
	return render(request, 'app/add_horas.html', contexto)
def Eliminarcobropieza(request):
	pieza=request.POST['id']
	piezaa=Piezas_usadas.objects.get(pk=pieza)
	piezaa.delete()
	return render(request, 'app/index.html')
def Eliminarcobrohora(request):
	hora=request.POST['idh']
	horaa=Horas.objects.get(pk=hora)
	horaa.delete()
	return render(request, 'app/index.html')
def Eliminardeposito(request):
	deposito=request.POST['idd']
	depositoo=Depositos.objects.get(pk=deposito)
	depositoo.delete()
	return render(request, 'app/index.html')
def venta_directa(request):
	contexto={}
	contexto['Piezas']=Piezas_en_inventario.objects.all()
	return render(request,'app/venta_directa.html' ,contexto)