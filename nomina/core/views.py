from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def form(request):
    empleado = ''
    fechaInicio = ''
    fechaFin = ''
    horasDiurnas = 0
    horasNocturnas = 0
    horasTotales = 0
    horasOrdinarias = 0
    extrasDiurnas = 0
    extrasNocturnas = 0
    recargosNocturnos = 0
    rNF = 0
    festivos = 0
    extrasDF = 0
    extrasNF = 0
    valorOrdinaria = 4833
    valorED = 6042
    valorEN = 8458
    valorRDF = 3625
    valorFestivo = 8458
    valorExtrasDF = 9665
    valorExtrasNF = 12081
    valorRN = 1692
    valorRNF = 5317
    valorDia = 38667
    auxTransporte = 4687
    if request.method == 'POST':
        empleado = request.POST['empleado']
        fechaInicio = request.POST['fechaInicio']
        fechaFin = request.POST['fechaFin']
        horasDiurnas = request.POST['horasDiurnas']
        horasNocturnas = request.POST['horasNocturnas']
        horasTotales = request.POST['horasTotales']
        horasOrdinarias = request.POST['horasOrdinarias']
        extrasDiurnas = request.POST['extrasDiurnas']
        extrasNocturnas = request.POST['extrasNocturnas']
        recargosNocturnos = request.POST['recargosNocturnos']
        festivos = request.POST.get('festivos')
        extrasDF = request.POST.get('extrasDF')
        extrasNF = request.POST.get('extrasNF')
        rNF = request.POST.get('RNF')
    fechaInicio = datetime.strptime(fechaInicio,'%Y-%m-%d')
    fechaFin = datetime.strptime(fechaFin, '%Y-%m-%d')
    dias = ((fechaFin-fechaInicio) / timedelta(days=1))+1 
    nomina = 0
    nomina = (dias*valorDia)+(float(extrasDiurnas)*valorED)+(float(extrasNocturnas)*valorEN)+(float(festivos)*valorRDF)+(float(extrasDF)*valorExtrasDF)+(float(extrasNF)*valorExtrasNF)+(float(recargosNocturnos)*valorRN)+(float(rNF)*valorRNF)+(dias*auxTransporte)
    descuentos = 0
    descuentos = (nomina*0.04)*2
    totalNomina = 0
    totalNomina = nomina - descuentos
    #(float(horasOrdinarias)*valorOrdinaria)
    print(nomina)
    return render(request, 'index.html',{'empleado':empleado, 'fechaInicio': fechaInicio, 'fechaFin': fechaFin,'total':nomina,'descuento': totalNomina})

def calcular(request):
    return render(request, "calculo.html")