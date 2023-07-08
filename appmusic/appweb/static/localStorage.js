const guardarEnLocalStorage = (clave, valor) => {
    localStorage.setItem(clave, valor);
}

const obtenerDeLocalStorage = (clave) => {
    return localStorage.getItem(clave);
}

const eliminarDeLocalStorage = (clave) => {
    localStorage.removeItem(clave);
}


const agregar = (producto) => {
    console.log("hola")
    let carrito = JSON.parse(obtenerDeLocalStorage("carrito"))

    carrito.push(producto)
    guardarEnLocalStorage("carrito", carrito);
    
}


