from ListaCliente import ListaCliente


newList = ListaCliente()

newList.agregarPrimero("Adam")
newList.agregarUltimo("Lucia")
newList.agregarUltimo("Carlos")
newList.agregarUltimo("Sam")

#Agregar elementos a la lista de compras
#Adam
cliente1 = newList.buscarCliente("Adam")
cliente1.compras.agregarPrimero(1, "Fresas", 15)
cliente1.compras.agregarUltimo(2, "Pollo", 30)
cliente1.compras.agregarUltimo(3, "Agua", 5)

#Lucia
newList.agregarCompra("Lucia", 1, "Lechuga", 15)
newList.agregarCompra("Lucia", 2, "Mani", 9)

#Carlos
newList.agregarCompra("Carlos", 1, "Salsa", 15)
newList.agregarCompra("Carlos", 2, "Queso", 22)
newList.agregarCompra("Carlos", 3, "Pan", 8)

#Sam
newList.agregarCompra("Sam", 1, "Jalea", 9)
newList.agregarCompra("Sam", 2, "Jamon", 24)

#Eliminar elementos
newList.eliminarCompra("Adam", 2)

newList.recorrer()
newList.graficar()