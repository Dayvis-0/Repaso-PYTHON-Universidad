# Ejemplo 4-7. Calculand Fibonacci n-simo usando recursividad lineal

def buen_fibonacci(n):
    """Devuelve un par de numero Fibonacci. F(n) y F(n-1)"""
    if n <= 1:
        return (n,0)
    else:
        (a, b) = buen_fibonacci(n-1)
        return (a+b, a)

    
