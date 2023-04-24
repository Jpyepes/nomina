const inputSelect = document.getElementById('inputGrande');
const inputCantidad = document.getElementById('inputCantidadSolicitada');
const inputMandarDatos = document.getElementById('mandarPython');
const verInfo = document.getElementById('infoListProductos');
var listaProductos = [];
function agregarElemento(){
    if(inputCantidad.value != ''){
    listaProductos.push(['['+inputSelect.value,inputCantidad.value+']']);
    console.log(listaProductos);
    verInfo.innerHTML = listaProductos;
    inputMandarDatos.value = listaProductos;
    inputSelect.value = '';
    inputCantidad.value = '';
    } else{
        verInfo.innerHTML = 'Por favor rellene el campo de cantidad solicitada';
    }
}

/*var listaProductos = [];
const inputSelect = document.getElementById('inputGrande');
function agregarProducto(){
    let contenedor = document.getElementById('contenedorCrearOrden');
    let section = document.getElementById('sectionPedidoOrden');
    let nuevaSection = section.cloneNode(true);
    contenedor.appendChild(nuevaSection);
    let botonesEliminar = document.getElementsByClassName('borrarProductoOrden');
    for(let i=0; i<botonesEliminar.length; i++){
        botonesEliminar[i].addEventListener('click', eliminarProducto);
    }
}
function eliminarProducto(event){
    let contenedor = document.getElementById('contenedorCrearOrden');
    let section = event.target.closest('.divFlex');
    contenedor.removeChild(section);
}

inputSelect.addEventListener('change', agregarLista);
function agregarLista(e){
    listaProductos.push(e.value);
    console.log(listaProductos);
}*/