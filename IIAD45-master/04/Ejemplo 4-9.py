# Ejemplo 4-9. Revierte los elementos de una secuencia

def revertir(S, start, stop):
    """Revierte los elementos de un slice S[start:stop]"""
    if start < stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        revertir(S, start+1, stop-1)
    