from django.shortcuts import render
from .models import Producto, ProductoOrden, OrdenProduccion
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
        data = request.POST.get('datosProducto')
        listaProductos = [data]
        print(type(data))
        print(data[0])
        print(listaProductos)
    return render(request, 'crearOrden.html')