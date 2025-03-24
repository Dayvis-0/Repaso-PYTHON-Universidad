# Ejemplo 3-2.  promedio prefijo con complejidad cuadratica

def promedio_prefijo1(S):
    """Devuelve una lista tal que para todos los elementos 
    A[j] son iguales al promedio de los anteriores S[0]..S[j]"""
    n = len(S)
    A = [0]*n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total / (j+1)
    return A
