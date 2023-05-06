from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Nomina
from .models import Empleado
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.
@login_required
def landing(request):
    userPedidos = False
    userP = False
    userAdm = False
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
        print(f"Perms --> {request.user.get_group_permissions()}")
        if request.user.username == 'jpyepes':
            userAdm = True
        if request.user.username == 'pedidoscr':
            userPedidos = True
        if request.user.username == 'produccioncr':
            userP = True

    else:
        print("User is not logged in :(")
    return render(request, 'landing.html', {'userP':userP,'userPedidos':userPedidos, 'userAdm':userAdm})

@login_required
def form(request):
    empleado = ''
    fechaInicio = '2023-03-17'
    fechaFin = '2023-03-17'
    extrasDiurnas = 0
    extrasNocturnas = 0
    recargosNocturnos = 0
    rNF = 0
    festivos = 0
    extrasDF = 0
    extrasNF = 0
    valorDia= 0
    valorHoraOrdinaria = 0
    diasLaborados = 0
    diasAuxilioT = 0
    msgError = 'Intentalo de nuevo'
    if request.method == 'POST':
        empleado = request.POST['empleado']
        fechaInicio = request.POST['fechaInicio']
        fechaFin = request.POST['fechaFin']
        diasLaborados = float(request.POST.get('diasLaborados'))
        diasAuxilioT = int(request.POST.get('diasAuxilioT'))
        extrasDiurnas = request.POST['extrasDiurnas']
        extrasNocturnas = request.POST['extrasNocturnas']
        recargosNocturnos = request.POST['recargosNocturnos']
        festivos = request.POST.get('festivos')
        extrasDF = request.POST.get('extrasDF')
        extrasNF = request.POST.get('extrasNF')
        rNF = request.POST.get('RNF')
    if empleado == '':
        return render(request, 'index.html',{'msgError':msgError})
    try:
        valorDia = int((int(salarioNombre(empleado))/240)*8)
        valorHoraOrdinaria = int(salarioNombre(empleado))/240
        print(salarioNombre(empleado))
    except:
        print('No hay ningún empleado')
    #fechaInicio = datetime.strptime(fechaInicio,"%Y-%m-%d")
    #fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d")
    #dias = ((fechaFin-fechaInicio) / timedelta(days=1))+1 
    valorED = valorHoraOrdinaria*1.25
    valorEN = valorHoraOrdinaria*1.75
    valorRDF = valorHoraOrdinaria*0.75
    valorExtrasDF = valorHoraOrdinaria*2
    valorExtrasNF = valorHoraOrdinaria*2.5
    valorRN = valorHoraOrdinaria*0.35
    valorRNF = 5317
    auxTransporte = 4687
    nominaC = 0
    nominaC = (diasLaborados*valorDia)+(float(extrasDiurnas)*valorED)+(float(extrasNocturnas)*valorEN)+(float(festivos)*valorRDF)+(float(extrasDF)*valorExtrasDF)+(float(extrasNF)*valorExtrasNF)+(float(recargosNocturnos)*valorRN)+(float(rNF)*valorRNF)+((diasAuxilioT)*auxTransporte)
    nominaSA = nominaC-((diasAuxilioT)*auxTransporte)
    descuentos = 0
    descuentos = (nominaSA*0.04)*2
    totalNomina = 0
    totalNomina = nominaC - descuentos
    form = Nomina(empleado = pkNombre(empleado),fechaInicio = fechaInicio,fechaFin = fechaFin,extrasDiurnas = extrasDiurnas,extrasNocturnas = extrasNocturnas,recargosNocturnos = recargosNocturnos,horasFestivas = festivos,extrasDF = extrasDF,extrasNF = extrasNF,rNF = rNF,devengado = nominaC, total = totalNomina)
    form.save()
    return render(request, 'index.html',{'empleado':empleado, 'fechaInicio': fechaInicio, 'fechaFin': fechaFin,'total':nominaC,'descuento': totalNomina})

@login_required
def crearEmpleado(request):
    nombre = ''
    if request.method == 'POST':
        nombre = request.POST.get('nombreEmpleadoC')
        cedula = request.POST.get('cedulaEmpleadoC')
        fechaInicio = request.POST.get('fechaInicioEmpleadoC')
        salarioBase = request.POST.get('salarioBaseEmpleadoC')
        f = Empleado(cedula = cedula, nombre = nombre, salarioBase = salarioBase, fechaInicio = fechaInicio)
        f.save()
    msgExito = f'¡El empleado {nombre} ha sido creado exitosamente!'
    return render(request, 'crearEmpleado.html',{'msgExito':msgExito, 'nombre':nombre})

@login_required
def actualizarEmpleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('empleadoA')
        salarioBase = request.POST.get('salarioBaseEmpleadoA')
        fechaFin = request.POST.get('fechaFinA')
        empleado = pkNombre(nombre)
        if salarioBase != '':
            empleado.salarioBase = salarioBase
        if fechaFin != '':
            empleado.fechaFin = fechaFin
        empleado.save()

    return render(request, 'actualizarEmpleado.html')

@login_required
def historialNomina(request):
    nombre = ''
    cedula = 0
    nomina = ''
    if request.method == 'POST':
        nombre = request.POST.get('empleadoH')
        nomina = Nomina.objects.filter(empleado = pkNombre(nombre))
        cedula = cedulaEmpleado(nombre)

    return render(request, 'historial.html', {'nombre': nombre, 'cedula': cedula, 'objetoNomina': nomina})

#-------------------------------------------------------------------------------------------------------------------------------------
def pkNombre(nombreE):
    empleado = Empleado.objects.get(nombre=nombreE)
    return empleado

def salarioNombre(nombreE):
    empleado = Empleado.objects.get(nombre=nombreE)
    salarioEmpleado = empleado.salarioBase
    return salarioEmpleado

def cedulaEmpleado(nombreE):
    empleado = Empleado.objects.get(nombre=nombreE)
    cedula = empleado.cedula
    return cedula
