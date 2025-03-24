# Revertir los elementos de una secuencia usando recursividad lineal

def revertir(S, start, stop):
    """Revierte los elementos de un slice [start, stop]"""
    
    if start < stop - 1: 
        
        S[start], S[stop - 1] = S[stop - 1], S[start]
        
        revertir(S, start+1, stop-1)
        
    return S
        
nume = [1,2,3]

print(revertir(nume, 0, len(nume)))