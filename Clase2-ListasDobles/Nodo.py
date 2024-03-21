class Libro:
    def __init__(self, codigo, titulo, autor) :
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor

        self.anterior = None
        self.siguiente = None