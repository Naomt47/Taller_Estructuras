from Nodo import Nodo
import os

class ListaCicular:
    def __init__(self):
        self.primero = None
        self.contador = 0
    
    #Insercion del elemento
    def insertar(self, elemento):
        if self.primero is None:
            self.primero = Nodo(elemento)
            self.primero.siguiente = self.primero
            self.contador += 1
        else:
            actual = self.primero
            if self.contador == 1:
                temporal = Nodo(elemento)
                actual.siguiente = temporal
                temporal.siguiente = self.primero
                self.contador += 1
            else:
                actual = self.primero
                for i in range(self.contador-1):
                    actual = actual.siguiente
                temporal = Nodo(elemento)
                actual.siguiente = temporal
                self.contador += 1
    
    def eliminar(self, elemento):
        if self.primero is None:
            print("La lista está vacía")
            return

        actual = self.primero
        previo = None

        # Buscar el nodo a eliminar
        while actual.siguiente != self.primero:
            if actual.dato == elemento:
                break
            previo = actual
            actual = actual.siguiente
        else:  # Si llega al final sin encontrar el elemento
            if actual.dato != elemento:
                print(f"Elemento {elemento} no encontrado en la lista")
                return

        # Si el elemento es el primero de la lista
        if previo is None:
            if self.contador == 1:
                self.primero = None
            else:
                temp = self.primero
                while temp.siguiente != self.primero.siguiente:
                    temp = temp.siguiente
                temp.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
        else:
            previo.siguiente = actual.siguiente

        self.contador -= 1
        print(f"Elemento {elemento} eliminado")

    def imprimir(self):
        temporal = self.primero
        while temporal is not None:
            print(temporal.dato)
            temporal = temporal.siguiente

    def graficar(self):
        codigo_dot = "digraph G {\nlabel=\" Lista Circular Simple \";\nnode[shape=box];\n"
        temporal = self.primero
        conexiones = ""
        nodos = ""
        numnodo = 0
        
        file = open("circular.dot", "w")
        
        for _ in range(self.contador):
            nodos += "N"+str(numnodo)+"[label=\""+temporal.dato+"\""+"];\n"
            if temporal.siguiente != self.primero:
                auxnum = (numnodo+1)%self.contador
                conexiones += "N"+str(numnodo)+" -> N"+str(auxnum)+";\n"
            temporal = temporal.siguiente
            numnodo += 1
        
        codigo_dot += nodos + "\n"
        codigo_dot += "{rank=same;\n"+conexiones+"}\n\n}"
        
        file.write(codigo_dot)
        file.close()
        os.system("dot -Tpng circular.dot -o circular.png")