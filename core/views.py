from django.shortcuts import render, redirect
from .models import Pastel
from .forms import PastelForm
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def somos(request):
    return render(request, 'somos.html')

def galeria(request):
    return render(request, 'galeria.html')

def login(request):
    return render(request, 'login.html')

def api(request):
    return render(request, 'api.html')

def reloj(request):
    return render(request, 'reloj.html')

# backendPasteles

def mostrar(request):
    #obtenemos todos los vehiculos almacenados en la clase
    pasteles = Pastel.objects.all()
    #creamos un diccionario
    datos={
        'tortas': pasteles
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrar.html', datos)

def eliminar(request, id):
    pastel = Pastel.objects.get(codigo=id)
    pastel.delete()
    return redirect('mostrar')

def crear(request):
    if request.method=='POST': 
        pastelform = PastelForm(request.POST, request.FILES)
        if pastelform.is_valid():
            pastelform.save()     #similar al insert
            return redirect('mostrar')
    else:
        pastelform=PastelForm()
    return render(request, 'crearPasteles.html', {'pastelform': pastelform})


def modificar(request, id):
    pastel = Pastel.objects.get(codigo=id) #buscamos el objeto x patente = id
    datos ={
        'form': PastelForm(instance=pastel) #instanciamos el obj. en un obj. de tipo formulario
    }
    #el siguiente bloque modifica el contenido del objeto almacenado
    if request.method=='POST':
        formulario = PastelForm(data=request.POST, instance=pastel)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    
    return render(request, 'modificar.html', datos)

#backendClientes

def mostrar1(request):
    #obtenemos todos los vehiculos almacenados en la clase
    clientes = Cliente.objects.all()
    #creamos un diccionario
    datos={
        'clientes': clientes
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrar1.html', datos)

def eliminar1(request, id1):
    cliente = Cliente.objects.get(rut=id1)
    cliente.delete()
    return redirect('mostrar1')

def crear1(request):
    if request.method=='POST': 
        clienteform = ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()     #similar al insert
            return redirect('mostrar1')
    else:
        clienteform=ClienteForm()
    return render(request, 'crear1.html', {'clienteform': clienteform})


def modificar1(request, id1):
    cliente = Cliente.objects.get(rut=id1) #buscamos el objeto x patente = id
    datos ={
        'form': ClienteForm(instance=cliente) #instanciamos el obj. en un obj. de tipo formulario
    }
    #el siguiente bloque modifica el contenido del objeto almacenado
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar1')
    
    return render(request, 'modificar1.html', datos)




