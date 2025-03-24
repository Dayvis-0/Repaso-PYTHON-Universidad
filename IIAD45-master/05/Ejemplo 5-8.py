# Ejemplo 5-8. Insertar-ordenar en una lista

def insertar_ordenar(A):
    """Ordenar una lista de elementos en orden no decreciente"""
    for k in range(1, len(A)):
        actual = A[k]
        j = k
        while j>0 and A[j-1]>actual:
            A[j] = A[j-1]
            j -= 1
        A[j] = actual
    
    return A