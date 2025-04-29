#Programa que clacule el factorial de un numero entero y positivo

"""C-omplejidad:
Temporal: O(n), porque se llama recursivamente x veces hasta llegar a x == 0
Espacial: O(n), porque hay n llamadas apiladas, ocupando memoria en pila"""
def factorialRecursiva(x: int) -> int:
    if x == 0:
        return 1
    else:
        return x * factorialRecursiva(x -1)
    
    
n = int(input("Numero entero y positivo: "))

"""Complejidad
Temporal: O(n), porque se recorre iterativamente x veces hasta llegar a x = x
Espacial: O(1), porque solo se hace una multiplicaicon cada iteracion"""
def factorialIterativa(x: int) -> int:
    res = 1
    
    for i in range(2, x+1):
        res *= i
    
    return res

if n >= 0:
    fac = factorialRecursiva(n)

    print(f"El factorial con recursividad de {n} es: {fac}\nEl factorial con iteracion es: {factorialIterativa(n)}")
else:
    print("El numero debe de ser positivo")