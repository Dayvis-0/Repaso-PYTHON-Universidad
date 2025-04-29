# Programa que calcule el mcd (MAximo Comun Civisor) de dos numeros 


"""Complejidad 
Temporal: O(log min(a, b)), cada iteracion reduce el tamaño de b al menos a la mitad en promedio
Espacial: O(n), solo usa variables simples"""
def MCDDeDosNumeros(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
        
    return a

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

print(f"El MCD de los dos numeros es: {MCDDeDosNumeros(n1, n2)}")