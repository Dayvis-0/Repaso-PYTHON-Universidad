# Ejemplo 4-8. Suman de elementos de una secuencia usando recursividad

def suma_lineal(S, n):
    """Devuelve la suma de los primeros n numeros de la secuencia S"""
    if n == 0:
        return 0
    else:
        return suma_lineal(S, n-1) + S[n-1]
    
    

    
