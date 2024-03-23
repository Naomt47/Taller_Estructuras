from Nodo import Nodo
import os

class Arbol_Binario:
    def __init__(self) -> None:
        self.raiz = None
    
    def poner(self, dato):
        self.raiz = self.add(dato, self.raiz)
    
    def add(self, dato, nodo):
        if nodo == None:
            return Nodo(dato)
        if dato.carnet < nodo.valor.carnet:
            nodo.izq = self.add(dato, nodo.izq)
        else:
            nodo.der = self.add(dato, nodo.der)
        
        return nodo
    
    def in_orden(self):
        self.in_orden_recursivo(self.raiz)
    
    def in_orden_recursivo(self, nodo):
        if nodo != None:
            self.in_orden_recursivo(nodo.izq)
            print(nodo.valor.carnet)
            self.in_orden_recursivo(nodo.der)
    
    def pre_orden(self):
        self.pre_orden_recursivo(self.raiz)
    
    def pre_orden_recursivo(self, nodo):
        if nodo != None:
            print(nodo.valor.carnet)
            self.pre_orden_recursivo(nodo.izq)
            self.pre_orden_recursivo(nodo.der)
    
    def post_orden(self):
        self.post_orden_recursivo(self.raiz)
    
    def post_orden_recursivo(self, nodo):
        if nodo != None:
            self.post_orden_recursivo(nodo.izq)
            self.post_orden_recursivo(nodo.der)
            print(nodo.valor.carnet)

    def generar_dot(self, filename):
        dot_file = open(filename, "w")
        dot_file.write('digraph G {')
        self._generar_dot_recursivo(self.raiz, dot_file)
        dot_file.write('}')
        dot_file.close()
        
        print(f"Archivo DOT generado como '{filename}'.")
        
        os.system("dot -Tpng "+filename+" -o "+filename+".png")
        
    def _generar_dot_recursivo(self, nodo, dot_file):
        if nodo is not None:
            dot_file.write(f'"{nodo.valor.nombre}" [label="{nodo.valor.nombre}\n{nodo.valor.carnet}"];\n')
            if nodo.izq is not None:
                dot_file.write(f'"{nodo.valor.nombre}" -> "{nodo.izq.valor.nombre}" [label="izq"];\n')
                self._generar_dot_recursivo(nodo.izq, dot_file)
            if nodo.der is not None:
                dot_file.write(f'"{nodo.valor.nombre}" -> "{nodo.der.valor.nombre}" [label="der"];\n')
                self._generar_dot_recursivo(nodo.der, dot_file)