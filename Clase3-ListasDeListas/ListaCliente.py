import os
from Cliente import Cliente


class ListaCliente:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def estaVacio(self):
        return self.primero == None
    
    def agregarPrimero(self, nombre):
        nuevo = Cliente(nombre)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
    
    def agregarUltimo(self, nombre):
        nuevo = Cliente(nombre)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    def buscarCliente(self, nombre):
        temp = self.primero
        while temp !=None:
            if temp.nombre == nombre:
                return temp
            temp = temp.siguiente
        
        return None

    def agregarCompra(self, nombre, cod, desc, precio):
        cliente = self.buscarCliente(nombre)
        if cliente != None:
            cliente.compras.agregarUltimo(cod, desc, precio)
        else:
            print("No existe el cliente "+nombre)
    
    def eliminarCompra(self, nombre, cod):
        cliente = self.buscarCliente(nombre)
        if cliente != None:
            cliente.compras.eliminar(cod)
        else:
            print("No existe el cliente "+nombre)
    
    def recorrer(self):
        temp = self.primero
        while temp!=None:
            print(temp.nombre)
            print("Lista de compras")
            temp.compras.recorrer()
            print("---------------------")
            temp = temp.siguiente
    
    def eliminar(self, nombre):
        temp = self.primero
        while temp!=None:
            if temp.nombre == nombre:
                if temp == self.primero:
                    self.primero = temp.siguiente
                    temp.siguiente = None
                    self.primero.anterior = None
                    break
                elif temp == self.ultimo:
                    self.ultimo = temp.anterior
                    temp.anterior = None
                    self.ultimo.siguiente = None
                    break
                else:
                    temp.anterior.siguiente = temp.siguiente
                    temp.siguiente.anterior = temp.anterior
                    temp.siguiente = None
                    temp.anterior = None
                    break
            temp = temp.siguiente
    
    def graficar(self):
        temp = self.primero
        contador = 0
        cadena = 'digraph G{\n rankdir=LR;\n'
        file = open("ListaDoble.dot", "w")
        while temp!=None:
            cadena += 'Nodo'+str(contador)+'[label="'+temp.nombre+'"];\n'
            cadena += temp.compras.graficar(temp.nombre)
            cadena += 'Nodo'+str(contador)+ '-> '+temp.nombre+"Nodo0;\n"
            if temp != self.primero:
                cadena += 'Nodo'+str(contador-1)+' -> Nodo'+str(contador)+';\n'
                cadena += 'Nodo'+str(contador)+' -> Nodo'+str(contador-1)+';\n'
            temp = temp.siguiente
            contador += 1
        
        cadena += 'rank = same {'
        for i in range(contador):
            cadena += 'Nodo'+str(i)+" "
        cadena += '}\n'

        file.write(cadena+"\n}")
        file.close()
        os.system("dot -Tpng ListaDoble.dot -o listaDoble.png")