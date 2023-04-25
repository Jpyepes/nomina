from django.shortcuts import render
from .models import Producto, ProductoOrden, OrdenProduccion
from datetime import datetime
# Create your views here.

def crearProducto (request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreProducto')
        stockUnidades = request.POST.get('stockUnidades')
        stockGramos = request.POST.get('stockGramos')
        precio = request.POST.get('precio')
        listaProducto = [nombre,stockUnidades,stockGramos,precio]
        for i in range(len(listaProducto)):
            if listaProducto[i] == '':
                listaProducto[i] = 0
        producto = Producto(nombre=listaProducto[0],stockUnidades=int(listaProducto[1]),stockGramos=float(listaProducto[2]),precio=float(listaProducto[3]))
        producto.save()
    return render(request, 'crearProducto.html')

def crearOrden(request):
    if request.method == 'POST':
        fechaEntrega = request.POST.get('fechaEntrega')
        data = request.POST.get('datosProducto')
        dataTratada = data.split(",")
        productos = []
        cantidad = []
        orden = OrdenProduccion(fechaCreacion=datetime.now(),fechaEntrega=fechaEntrega)
        orden.save()
        try:
            for i in range(len(dataTratada)):
                if i % 2 == 0:
                    productos.append(dataTratada[i])
                else:
                    cantidad.append(dataTratada[i])    
        except:
            print('Ha ocurrido un error, vuelva a intentarlo más tarde')

        for i in range(len(productos)):
            relacionProducto = pkNombre(productos[i])
            varAux = ProductoOrden(cantidadSolicitada=cantidad[i],precio=calcularPrecioPO(productos[i],cantidad[i]),producto=relacionProducto,ordenProduccion=orden)
            varAux.save()
            relacionProducto.lote = relacionProducto.lote + 1
            relacionProducto.save()

    return render(request, 'crearOrden.html')

def verOrden(request):
    ordenes = ProductoOrden.objects.all().order_by('-ordenProduccion__id')
    datos_por_orden = {}
    fecha_creacion = None
    fecha_entrega = None
    for objeto in ordenes:
        id_orden = objeto.ordenProduccion.id
        nombre_producto = objeto.producto.nombre
        cantidad = objeto.cantidadSolicitada

        fechas = OrdenProduccion.objects.get(id=id_orden)
        fecha_creacion = fechas.fechaCreacion
        fecha_entrega = fechas.fechaEntrega
        if id_orden not in datos_por_orden:
            datos_por_orden[id_orden] = {'productos': [],'fecha_creacion': fecha_creacion, 'fecha_entrega': fecha_entrega}
        datos_por_orden[id_orden]['productos'].append({'nombre': nombre_producto, 'cantidad': cantidad})

    # Crear un contexto con los datos de cada orden de producción
    context = {'datos_por_orden': datos_por_orden, 'fechaCreacion': fecha_creacion,'fechaEntrega': fecha_entrega}
    return render(request, 'verOrden.html', context)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def pkNombre(nombreP):
    producto = Producto.objects.get(nombre=nombreP)
    return producto
def getObjOrdenes(idPO):
    orden = OrdenProduccion.objects.get(id=idPO.id)
    return orden
def calcularPrecioPO(nombreP,cantidadS):
    producto = Producto.objects.get(nombre=nombreP)
    precio = int(producto.precio) * int(cantidadS)
    return precio
