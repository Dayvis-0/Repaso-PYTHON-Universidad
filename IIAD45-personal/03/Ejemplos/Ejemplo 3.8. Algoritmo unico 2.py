# Algoritmo unico 2

def unique2(S):
    """Devuelve True si no hay elementos duplicados en la secuencia S"""
    
    temp = sorted(S)
    
    for i in range(len(temp)):
        if S[i-1]  == S[i]:
            return False
        
    return True

numbers = [1,2,3,4,5]

print(unique2(numbers))