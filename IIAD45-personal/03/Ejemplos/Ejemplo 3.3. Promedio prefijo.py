# Algoritmo promedio prefijo con complejidad cuadratica

def avarage_prefix2(S):
    """Devuelve una lista tal que para todos los elementos 
    A[i] son iguales al promedio de los anteriores S[0]...S[j]"""
    
    n = len(S)
    A = [0]*n
    
    for i in range(n):
        A[i] = sum(S[0:i+1]) / (i + 1)
        
    return A

numbers = [1,2,3,4,5]

print(f'Lista de los promedios de los anteriores: {avarage_prefix2(numbers)}')