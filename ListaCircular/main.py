from Cancion import Cancion
from ListaCircular import ListaCicular

cancion1 = Cancion("Shape of You", "Ed Sheeran", "÷ (Divide)")
cancion2 = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera")
cancion3 = Cancion("Hotel California", "Eagles", "Hotel California")
cancion4 = Cancion("Rolling in the Deep", "Adele", "21")

lst_c = ListaCicular()

lst_c.insertar(cancion1.nombre)
lst_c.insertar(cancion2.nombre)
lst_c.insertar(cancion3.nombre)
lst_c.insertar(cancion4.nombre)

lst_c.imprimir()

print("==========================================================")

lst_c.eliminar(cancion1.nombre)
lst_c.eliminar(cancion2.nombre)
lst_c.imprimir()