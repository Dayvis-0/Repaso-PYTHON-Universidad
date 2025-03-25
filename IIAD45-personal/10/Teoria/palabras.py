# -*- coding: utf-8 -*-
"""
Contar la cantidad de veces que ocurre cada palabra en el libro en txt
mostrar la que tiene mas repeticiones y cuantas veces ses repite
"""

archivo = open("el_quijote.txt", encoding="utf-8")
lineas = archivo.readlines()
palabras = ' '.join(lineas).lower().split()

def quitapuntuacion(s):
    simbolos = ".,:"
    snueva = ''.join( c for c in s if c not in simbolos)
    return snueva

palabras = map(quitapuntuacion, palabras)

conteo = {}

for p in palabras:
    if p in conteo:
        conteo[p] += 1
    else:
        conteo[p] = 1

maximo = 0
mayor = ""

for c in conteo:
    if conteo[c] >= maximo:
        maximo = conteo[c]
        mayor = c

print(mayor, maximo)

