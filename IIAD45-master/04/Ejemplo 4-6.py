# Ejemplo 4-6. Calculand Fibonacci n-simo usando recursividad

def mal_fibonacci(n):
    """Devuelve el n-simo numero Fibonacci"""
    if n <= 1:
        return n
    else:
        return mal_fibonacci(n-2) + mal_fibonacci(n-1)
    
