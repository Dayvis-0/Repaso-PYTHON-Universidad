# Ejemplo 4-9. Revierte los elementos de una secuencia

def power(x, n):
    """Calcula el valor de x**n"""
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)
    