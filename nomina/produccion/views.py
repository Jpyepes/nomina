from django.shortcuts import render
from .models import Producto, ProductoOrden, OrdenProduccion
from datetime import datetime
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.

@login_required
def crearProducto (request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreProducto')
        stock = request.POST.get('stock')
        unidades = request.POST.get('unidades')
        precio = request.POST.get('precio')
        und = 'Und'
        if unidades == 'on':
            und = 'Gr'
        listaProducto = [nombre,stock,und,precio]
        for i in range(len(listaProducto)):
            if listaProducto[i] == '':
                listaProducto[i] = 0
        producto = Producto(nombre=listaProducto[0],stock=int(listaProducto[1]),unidades=und,precio=float(listaProducto[3]))
        producto.save()
    return render(request, 'crearProducto.html')

@login_required
@permission_required('produccion.add_ordenproduccion')
def crearOrden(request):
    fechaActual = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'POST':
        fechaEntrega = request.POST.get('fechaEntrega')
        data = request.POST.get('datosProducto')
        dataTratada = data.split(",")
        productos = []
        cantidad = []
        orden = OrdenProduccion(fechaCreacion=datetime.now(),fechaEntrega=fechaEntrega,ordenCompletada='0')
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

    return render(request, 'crearOrden.html',{'fechaActual': fechaActual})

@login_required
@permission_required('produccion.change_ordenproduccion')
def verOrden(request):
    completarOrden(request)
    maxZero = 6
    ordenes = ProductoOrden.objects.all().order_by('-ordenProduccion__id')
    datos_por_orden = {}
    fecha_creacion = None
    fecha_entrega = None
    for objeto in ordenes:
        objOrden = OrdenProduccion.objects.get(id=objeto.ordenProduccion.id)
        if objOrden.ordenCompletada != '1' and objOrden.ordenDespacho != '1':
            id_orden = objeto.ordenProduccion.id
            nombre_producto = objeto.producto.nombre
            lote_producto = str(objeto.producto.lote).zfill(maxZero-len(str(objeto.producto.lote)))
            und_producto = objeto.producto.unidades
            cantidad = objeto.cantidadSolicitada
            id_producto_orden = objeto.id
            cantidad_producida = objeto.cantidadProducida

            fecha_creacion = objOrden.fechaCreacion
            fecha_entrega = objOrden.fechaEntrega
            if id_orden not in datos_por_orden:
                datos_por_orden[id_orden] = {'productos': [],'fecha_creacion': fecha_creacion, 'fecha_entrega': fecha_entrega}
            datos_por_orden[id_orden]['productos'].append({'nombre': nombre_producto, 'cantidad': cantidad,'lote': lote_producto, 'unidades':und_producto, 'idProductoOrden':id_producto_orden, 'cantidadProducida':cantidad_producida})

    # Crear un contexto con los datos de cada orden de producción
    context = {'datos_por_orden': datos_por_orden, 'fechaCreacion': fecha_creacion,'fechaEntrega': fecha_entrega}
    return render(request, 'verOrden.html', context)

@login_required
def completarOrden(request):
    if request.method == 'POST':
        adelantoProduccion = request.POST.get('datosProduccion')
        idOrden = request.POST.get('guardarAdelanto')
        dataTratada = adelantoProduccion.split(",")
        idProducto = []
        cantidadProducida = []
        try:
            for i in range(len(dataTratada)):
                if i % 2 == 0:
                    idProducto.append(dataTratada[i])
                else:
                    cantidadProducida.append(dataTratada[i])    
        except:
            print('Ha ocurrido un error, vuelva a intentarlo más tarde')

        for i in range(len(idProducto)):
            try:
                if idProducto[i] != '':
                    orden = OrdenProduccion.objects.get(id=idOrden)
                    objProductoOrden = ProductoOrden.objects.get(id=idProducto[i])
                    objProducto = Producto.objects.get(id=objProductoOrden.producto.id)
                    if orden.id == objProductoOrden.ordenProduccion.id:
                        objProductoOrden.cantidadProducida += int(cantidadProducida[i])
                        objProductoOrden.save() 
                        objProducto.stock +=  int(cantidadProducida[i])
                        objProducto.save()
            except:
                print(f"No hay productos con el id {idProducto[i]}")
        try:
            productosOrden = orden.devolverProductos()
            varAux = True
            for producto in productosOrden:
                if producto.cantidadProducida < producto.cantidadSolicitada: 
                    varAux = False
            if varAux:
                orden.ordenCompletada = '1'
                orden.save()
        except:
            print(f'No hay una orden de produccion con el id {idOrden}')
            
        
@login_required
@permission_required('produccion.change_ordenproduccion')
def verPedido(request):
    ordenes = ProductoOrden.objects.all().order_by('-ordenProduccion__id')
    datos_por_orden = {}
    fecha_creacion = None
    fecha_entrega = None
    for objeto in ordenes:
        objOrden = OrdenProduccion.objects.get(id=objeto.ordenProduccion.id)
        if objOrden.ordenCompletada != '1' and objOrden.ordenDespacho != '1' :
            id_orden = objeto.ordenProduccion.id
            nombre_producto = objeto.producto.nombre
            stock_producto = objeto.producto.stock
            und_producto = objeto.producto.unidades
            cantidad = objeto.cantidadSolicitada

            fecha_creacion = objOrden.fechaCreacion
            fecha_entrega = objOrden.fechaEntrega
            if id_orden not in datos_por_orden:
                datos_por_orden[id_orden] = {'productos': [],'fecha_creacion': fecha_creacion, 'fecha_entrega': fecha_entrega}
            datos_por_orden[id_orden]['productos'].append({'nombre': nombre_producto, 'cantidad': cantidad,'stock': stock_producto, 'unidades':und_producto})

    # Crear un contexto con los datos de cada orden de producción
    context = {'datos_por_orden': datos_por_orden, 'fechaCreacion': fecha_creacion,'fechaEntrega': fecha_entrega}
    return render(request, 'verPedido.html', context)

def inventario(request):
    maxZero = 6
    productos = Producto.objects.all()
    listaProductos = []
    for producto in productos:
       listaProductos.append({'nombre':producto.nombre,'stock':producto.stock,'und': producto.unidades,'lote':str(producto.lote).zfill(maxZero-len(str(producto.lote)))})
    return render(request, 'inventario.html', {'productos':listaProductos})

@login_required
@permission_required('produccion.add_ordenproduccion')
def ordenDespacho(request):
    msgExito = ''
    if request.method == 'POST':
        data = request.POST.get('datosProducto')
        dataTratada = data.split(",")
        productos = []
        cantidad = []
        orden = OrdenProduccion(fechaCreacion=datetime.now(),fechaEntrega=datetime.now(),ordenCompletada='0', ordenDespacho='1')
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
        msgExito = '¡Orden creada satisfactoriamente!'
    return render(request, 'ordenDespacho.html',{'msgExito':msgExito})

@login_required
@permission_required('produccion.change_ordenproduccion')
def verOrdenDespacho(request):
    completarOrdenDespacho(request)
    userAdm = False
    if request.user.is_authenticated:
        if request.user.username == 'jpyepes' or request.user.username == 'pedidoscr':
            userAdm = True
    ordenes = ProductoOrden.objects.all().order_by('-ordenProduccion__id')
    datos_por_orden = {}
    fecha_creacion = None
    fecha_entrega = None
    for objeto in ordenes:
        objOrden = OrdenProduccion.objects.get(id=objeto.ordenProduccion.id)
        if objOrden.ordenCompletada == '0' and objOrden.ordenDespacho == '1' and objOrden.ordenDespachoCompletada == '0':
            id_orden = objeto.ordenProduccion.id
            nombre_producto = objeto.producto.nombre
            und_producto = objeto.producto.unidades
            cantidad = objeto.cantidadSolicitada
            stock = objeto.producto.stock

            fecha_creacion = objOrden.fechaCreacion
            fecha_entrega = objOrden.fechaEntrega
            if id_orden not in datos_por_orden:
                datos_por_orden[id_orden] = {'productos': [],'fecha_creacion': fecha_creacion, 'fecha_entrega': fecha_entrega}
            datos_por_orden[id_orden]['productos'].append({'nombre': nombre_producto, 'cantidad': cantidad, 'unidades':und_producto, 'inventario':stock})

    # Crear un contexto con los datos de cada orden de producción
    context = {'datos_por_orden': datos_por_orden, 'fechaCreacion': fecha_creacion,'fechaEntrega': fecha_entrega, 'userAdm':userAdm}
    return render(request, 'verOrdenDespacho.html', context)

def completarOrdenDespacho(request):
    msgError= ''
    varAux = True
    if request.method == 'POST':
        idOrden = request.POST.get('completarOrdenDespacho')
        productosOrden = ProductoOrden.objects.filter(ordenProduccion = idOrden)
        orden = OrdenProduccion.objects.get(id=idOrden)
        for producto in productosOrden:
            try:
                objProducto = Producto.objects.get(id=producto.producto.id)
                cantidadSolicitada = producto.cantidadSolicitada
                if objProducto.stock >= cantidadSolicitada:
                    objProducto.stock = objProducto.stock - cantidadSolicitada
                    objProducto.save()
                else:
                    varAux=False
                    msgError = f'No hay suficiente stock de {objProducto.nombre}'
            except:
                print('No se encontro el producto')
        if varAux:
            orden.ordenDespachoCompletada = '1'
            orden.save()

            
    return msgError
            


      
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
