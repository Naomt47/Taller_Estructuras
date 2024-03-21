import os
from Nodo import Libro


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def estaVacio(self):
        return self.primero == None
    
    def agregarPrimero(self, codigo, titulo, autor):
        nuevo = Libro(codigo, titulo, autor)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
    
    def agregarUltimo(self, codigo, titulo, autor):
        nuevo = Libro(codigo, titulo, autor)
        if self.estaVacio():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    def recorrer(self):
        temp = self.primero
        while temp!=None:
            print(temp.codigo, temp.titulo, temp.autor)
            temp = temp.siguiente
    
    def eliminar(self, codigo):
        temp = self.primero
        while temp!=None:
            if temp.codigo == codigo:
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
        cadena = 'digraph G{'
        file = open("ListaDoble.dot", "w")
        while temp!=None:
            cadena += 'Nodo'+str(contador)+'[label="'+temp.titulo+'"];'
            if temp != self.primero:
                cadena += 'Nodo'+str(contador-1)+' -> Nodo'+str(contador)+';'
                cadena += 'Nodo'+str(contador)+' -> Nodo'+str(contador-1)+';'
            temp = temp.siguiente
            contador += 1
        file.write(cadena+"}")
        file.close()
        os.system("dot -Tpng ListaDoble.dot -o listaDoble.png")