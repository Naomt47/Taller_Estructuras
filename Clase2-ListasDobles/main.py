from ListaDoble import ListaDoble


newList = ListaDoble()

newList.agregarPrimero(1, "Las cronicas de narnia", "C.S. Lewis")
newList.agregarPrimero(2, "Maria", "Jorge Isaacs")
newList.agregarPrimero(3, "Cinco semanas en globo", "Julio Verne")
newList.agregarUltimo(4, "Renegados", "Marissa Meyer")

#newList.eliminar(1)
newList.recorrer()

newList.graficar()