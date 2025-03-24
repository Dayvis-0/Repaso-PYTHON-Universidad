# Promedio preefijo con comlejidad cuadratica

def avarage_prefix(S):
    """Devuelve una lista tal que para todos los elementos 
    A[j] son iguales al promedio de los anteriores data S[0]...S[i]"""
    
    n = len(S)
    A = [0]*n
    
    for i in range(n):
        total = 0
        for j in range(i+1):
            total += S[j]
            
        A[i] = total / (i+1)
        
    return A

numbers = [1,2,3,4,5]

print(f'Lista de los promedios de los anteriores: {avarage_prefix(numbers)}')