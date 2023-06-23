import { guardarEnLocalStorage, obtenerDeLocalStorage }  from '../localStorage'


const agregar = (producto) => {
    console.log("hola")
    let carrito = JSON.parse(obtenerDeLocalStorage("carrito"))

    carrito.push(producto)
    guardarEnLocalStorage("carrito", carrito);
}
