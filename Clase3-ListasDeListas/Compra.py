class Compra():
    def __init__(self, codigo, nombre, precio):
        #DATO
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

        #APUNTADORES
        self.siguiente = None