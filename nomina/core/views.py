from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Nomina
from .models import Empleado
# Create your views here.
def landing(request):
    return render(request, 'landing.html')

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
    valorED = 6042
    valorEN = 8458
    valorRDF = 3625
    valorExtrasDF = 9665
    valorExtrasNF = 12081
    valorRN = 1692
    valorRNF = 5317
    auxTransporte = 4687
    valorDia= 0
    diasLaborados = 0
    msgError = 'Intentalo de nuevo'
    if request.method == 'POST':
        empleado = request.POST['empleado']
        fechaInicio = request.POST['fechaInicio']
        fechaFin = request.POST['fechaFin']
        diasLaborados = int(request.POST.get('diasLaborados'))
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
        print(salarioNombre(empleado))
    except:
        print('No hay ningún empleado')
    #fechaInicio = datetime.strptime(fechaInicio,"%Y-%m-%d")
    #fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d")
    #dias = ((fechaFin-fechaInicio) / timedelta(days=1))+1 
    nominaC = 0
    nominaC = (diasLaborados*valorDia)+(float(extrasDiurnas)*valorED)+(float(extrasNocturnas)*valorEN)+(float(festivos)*valorRDF)+(float(extrasDF)*valorExtrasDF)+(float(extrasNF)*valorExtrasNF)+(float(recargosNocturnos)*valorRN)+(float(rNF)*valorRNF)+((diasLaborados)*auxTransporte)
    nominaSA = nominaC-((diasLaborados)*auxTransporte)
    descuentos = 0
    descuentos = (nominaSA*0.04)*2
    totalNomina = 0
    totalNomina = nominaC - descuentos
    form = Nomina(empleado = pkNombre(empleado),fechaInicio = fechaInicio,fechaFin = fechaFin,extrasDiurnas = extrasDiurnas,extrasNocturnas = extrasNocturnas,recargosNocturnos = recargosNocturnos,horasFestivas = festivos,extrasDF = extrasDF,extrasNF = extrasNF,rNF = rNF,devengado = nominaC, total = totalNomina)
    form.save()
    return render(request, 'index.html',{'empleado':empleado, 'fechaInicio': fechaInicio, 'fechaFin': fechaFin,'total':nominaC,'descuento': totalNomina})


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

def historialNomina(request):
    return render(request, 'historial.html')

#-------------------------------------------------------------------------------------------------------------------------------------
def pkNombre(nombreE):
    empleado = Empleado.objects.get(nombre=nombreE)
    return empleado

def salarioNombre(nombreE):
    empleado = Empleado.objects.get(nombre=nombreE)
    salarioEmpleado = empleado.salarioBase
    return salarioEmpleado