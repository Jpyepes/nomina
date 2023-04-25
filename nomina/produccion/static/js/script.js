const inputSelect = document.getElementById('inputGrande');
const inputCantidad = document.getElementById('inputCantidadSolicitada');
const inputMandarDatos = document.getElementById('mandarPython');
const verInfo = document.getElementById('infoListProductos');
var listaProductos = [];
function agregarElemento(){
    verInfo.innerHTML='';
    if(inputCantidad.value != ''){
    listaProductos.push([inputSelect.value,inputCantidad.value]);
    console.log(listaProductos);
    for(let i = 0;i<listaProductos.length;i++){
        let producto = document.createElement("div");
        producto.setAttribute("class","verInfoProducto");
        producto.innerHTML = "Producto: "+listaProductos[i][0]+" - Cantidad: "+listaProductos[i][1];
        verInfo.appendChild(producto);
    }
    //verInfo.innerHTML = listaProductos;
    inputMandarDatos.value = listaProductos;
    inputSelect.value = '';
    inputCantidad.value = '';
    } else{
        verInfo.innerHTML = 'Por favor rellene el campo de cantidad solicitado';
    }
}
