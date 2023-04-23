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
