# Ejemplo 3-8. Algoritmo unico2

def unico2(S):
    """Devuelve True si no hay elementos duplicados en la secuencia S"""
    temp = sorted(S)
    for j in range(len(temp)):
        if S[j-1] == S[j]:
            return False
    return True
