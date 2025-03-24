# Ejemplo 3-5. Algoritmo disjunto1

def disjunto1(A, B, C):
    """Devuelve True si no hay un elemento comun a todas las listas"""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True
