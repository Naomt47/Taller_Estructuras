from ListaSimple import ListaSimple

newList = ListaSimple()

newList.agregarPrimero(1,"chocolate",10.00)
newList.agregarPrimero(2,"galletas",15.00)
newList.agregarPrimero(3,"salsita",8.50)
newList.agregarUltimo(4, "fideos",3.75)

newList.recorrer()
newList.graficar("simple1")

# ELIMINAR UN NODO DE EN MEDIO
newList.eliminar(1)
newList.graficar("delete1")

