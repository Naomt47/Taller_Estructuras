from ABB import Arbol_Binario
from Estudiantes import Estudiante

e1 = Estudiante("abdul", 201807169)
e2 = Estudiante("kathy", 202100075)
e3 = Estudiante("angely", 202103095)
e4 = Estudiante("luis", 202010814)
e5 = Estudiante("erick", 201900621)
e6 = Estudiante("ortega", 201900597)

abb = Arbol_Binario()

abb.poner(e1)
abb.poner(e2)
abb.poner(e3)
abb.poner(e4)
abb.poner(e5)
abb.poner(e6)

print("=========================================")
print("In Orden")

abb.in_orden()

print("=========================================")
print("Pre Orden")

abb.pre_orden()

print("=========================================")
print("Post Orden")

abb.post_orden()

abb.generar_dot("arbol.dot")