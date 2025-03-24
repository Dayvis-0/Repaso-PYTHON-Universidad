# Ejemplo 3-6. Algoritmo disjunto2

def disjunto2(A, B, C):
    """Devuelve True si no hay un elemento comun a todas las listas"""
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True
