from ListaCompra import ListaCompra


class Cliente:
    def __init__(self, nombre):
        #Dato
        self.nombre = nombre
        self.compras = ListaCompra()

        #Apuntadores
        self.anterior = None
        self.siguiente = None