const inputDatos = document.getElementsByClassName('adelantoProduccion');
const inputMandarDatos = document.getElementById('mandarPython');
var listaProduccion = [];
function adelantoProduccion(){
    if (window.history.replaceState) { // verificamos disponibilidad
        window.history.replaceState(null, null, window.location.href);
    }
    for(let i = 0; i < inputDatos.length; i++){
        if(inputMandarDatos.value == ''){
            listaProduccion.push([inputDatos[i].getAttribute('id'),inputDatos[i].value]);
            console.log(listaProduccion)
        }
    }
    inputMandarDatos.value = listaProduccion;
    //verInfo.innerHTML = listaProductos;
}
console.log(listaProduccion);
