import os
from Nodo import Compra

class ListaSimple():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero  == self.ultimo == None
    
    def agregarPrimero(self, codigo, nombre, precio):
        nuevo = Compra(codigo, nombre, precio)
        if self.estaVacia() == True:
            self.primero  = self.ultimo = nuevo
        else:
            temp = nuevo
            temp.siguiente = self.primero
            self.primero = temp
        
    def agregarUltimo(self, codigo, nombre, precio):
        nuevo = Compra(codigo, nombre, precio)
        if self.estaVacia() == True:
            self.primero = self.ultimo = nuevo
        else:
            temp = nuevo
            self.ultimo.siguiente = temp
            self.ultimo = temp

    def recorrer(self):
        temp = self.primero
        while temp != None:
            print(temp.codigo, temp.nombre, temp.precio)
            temp = temp.siguiente

    def eliminar(self, codigo):
        temp1 = self.primero
        temp2 = None
        while temp1 != None:
            if temp1.codigo == codigo:
                if temp1 == self.primero:
                    temp2 = self.primero
                    temp1 = temp1.siguiente
                    self.primero = temp1
                    temp2.siguiente = None
                    break
                elif temp1 == self.ultimo: 
                    self.ultimo = temp2
                    temp2.siguiente = None
                    break
                else : 
                    temp2.siguiente = temp1.siguiente
                    temp1.siguiente = None
                    break
            else:
                temp2 = temp1
                temp1 = temp1.siguiente
    
    def graficar(self, name):
        temp = self.primero
        contador = 0
        file = open(name+".dot", "w")
        cadena = "digraph G{ \n"
        cadena += "rankdir=LR\n"
        cadena += "node[shape=square, shape = record, style=\"filled\", color=\"black\", fillcolor=\"yellow:green\"];"
        while temp != None:
            cadena += "Nodo"+str(contador)+"[label=\"" + str(temp.codigo)+" | "+ temp.nombre+ " | "+ str(temp.precio) + "\"];\n"
            if temp != self.primero:
                cadena += "Nodo"+str(contador-1)+" -> Nodo"+str(contador)+";\n"
            temp = temp.siguiente
            contador += 1
        
        cadena += "}"
        file.write(cadena)
        file.close()
        os.system("dot -Tpng "+ name+".dot -o "+name+".png")


