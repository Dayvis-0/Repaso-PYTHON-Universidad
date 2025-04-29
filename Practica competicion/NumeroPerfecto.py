""" Escribe un programa que detemrine si un numero es eperfecto o no
Un numero peerfecto se denomina perfecto cuando es igual a la suma de todos sus divisiores, ecepto el mismo
Por ejemplo: 28 = 1+2+4+7+14 """

"""Complejidad
Temporal: O(n) El bucle necesit ejecutar hasta n // 2
Espacial: O(1) La memoria usana no crececon el tamaño de n"""
def esPerfecto(x: int) -> bool:
    resu = 0
    
    for j in range(1, n//2 + 1):
        if n % j == 0:
            resu += j

    if n == resu:
        return True
    
    return False

n = int(input("Numero positivo y entero: "))

if n >= 0:
        
    if esPerfecto(n):
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")
else:
    print("El numero debe de ser positivo")