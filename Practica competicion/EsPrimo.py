# Algoritmo que diga si un numero entero positivo es primo o no

import math

"""Complejidad:
Temporal: O(raizn), el bucle ejecuta como mucho raiz n / 2 veces 
Espacil: O(1), la memoria usada se mantiene constante"""
def esPrimo(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    
    for j in range(3, int(math.sqrt(x)) + 1, 2):
        if x % j == 0:
            return False

    return True

n = int(input("Numero positivo y entero: "))

if n >= 0:
    if esPrimo(n):
        print("Es primo")
    else:
        print("No es primo") 
else:
    print("El numero debe de ser positivo")
    