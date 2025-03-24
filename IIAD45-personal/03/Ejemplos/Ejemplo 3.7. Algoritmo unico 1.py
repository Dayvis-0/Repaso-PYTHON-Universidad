# Algoritmo unico

def unique1(S):
    """Devuelve True si no hay elementos duplicados en la secuencia S"""
    
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if S[i] == S[j]:
                return False
            
    return True

numbers = [1,2,3,4,5]

print(unique1(numbers))