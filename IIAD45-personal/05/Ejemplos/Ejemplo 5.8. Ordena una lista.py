# Insertarordenar en una lista

def insertar_ordenar(A):
    """Ordenar una lista de elementos en orden no creciente"""
    
    for j in range(1, len(A)):
        actual = A[j]
        k = j
        
        while k > 0 and A[k-1] > actual:
            A[k] = A[k - 1]
            k -= 1
            
        A[k] = actual
    
    return A
        
print(insertar_ordenar([1,5,4]))