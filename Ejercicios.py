import random

# Ejercicio 1:
mi_lista = ["monte", "sol", "agua", "flor", "estrella"]
mi_tupla = ("montaña", "sol", "agua", "flor", "estrella")
mi_entero = 42
mi_diccionario = {'a': "montaña", 'b': "sol", 'c': "agua", 'd': "flor", 'e': "estrella"}

# Decimal usando libreria
from decimal import Decimal
mi_decimal = Decimal('3.14')  # Se puede utilizar un número string para crear un Decimal

print(mi_decimal)

# Ejercicio 2:
mi_flotante = 3.14159

# Redondear hacia arriba
import math
flotante_redondeado = math.ceil(mi_flotante)

print(flotante_redondeado)


# Ejercicio 3: 
from math import sqrt
raiz_cuadrada = sqrt(mi_flotante)

# Ejercicio 4: 
primer_elemento_diccionario = next(iter(mi_diccionario.values()))

# Ejercicio 5: 
segundo_elemento_tupla = mi_tupla[1]

# Ejercicio 6:
mi_lista.append("nube")

# Ejercicio 7: 
mi_lista[0] = "arboles"

# Ejercicio 8: 
mi_lista.sort()

# Ejercicio 9: 
mi_tupla += ("rio",)

# Imprimir los resultados de cada ejercicio
print("Lista:", mi_lista)
print("Tupla:", mi_tupla)
print("Flotante redondeado:", flotante_redondeado)
print("Raiz cuadrada del flotante:", raiz_cuadrada)
print("Primer elemento del diccionario:", primer_elemento_diccionario)
print("Segundo elemento de la tupla:", segundo_elemento_tupla)
