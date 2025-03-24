# Ejemplo 3-7. Algoritmo unico1

def unico1(S):
    """Devuelve True si no hay elementos duplicados en la secuencia S"""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True
