# Algoritmo de complejidad n

def avarage_prefix3(S):
    """Devuelve una lista tal que todos los elementos 
    A[i] son iguales al promedio de los anteriores S[0]...S[i]"""
    
    n = len(S)
    A = [0]*n
    total = 0
    
    for i in range(n):
        total += S[i]
        A[i] = total / (i + 1)
        
    return A

numbers = [1,2,3,4,5]

print(f'El mas grande de los numeros es: {avarage_prefix3(numbers)}')