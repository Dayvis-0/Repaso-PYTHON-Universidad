# Programa que genera una lista de los N primeros numeros primos
import math

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

"""Complejidad
Temporal: O(n x n log n)
Espacial: O(n)"""

def NPrimos(n: int) -> list[int]:
    nprimos = []
    i = 2
    cont = 0
    
    while cont != n:
        if esPrimo(i):
            cont += 1
            nprimos.append(i) 
        i += 1    

    return nprimos
        
n = int(input("Cantidad de primos: "))

if n >= 0:
    if n == 0:
        print("No hay numeros primos")
    else:
        print(NPrimos(n))
else:
    print("La cantidad debe de ser positivo")