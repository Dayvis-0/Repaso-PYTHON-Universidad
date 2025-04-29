# Programa que genera una lista de los N primeros numeros primos
import math

def esPrimo(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return True
    
    for j in range(3, int(math.sqrt(x)) + 1, 2):
        if x % j == 0:
            return False
        
    return True

def NPrimos(n: int) -> list[int]:
    nprimos = []
    i = 2
    cont = 0
    
    while cont != n:
        if esPrimo(i):
            cont += 1
            nprimos.append(i)    

    return nprimos
        
        
n = int(input("Cantidad de primos: "))

if n >= 0:
    if n == 0:
        print("No hay numeros primos")