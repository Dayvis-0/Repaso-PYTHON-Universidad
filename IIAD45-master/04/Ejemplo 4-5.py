# Ejemplo 4-5. unico3 recursivo

def unico3(S, start, stop):
    """Devuelve True si no hay elementos duplicados en el slice S[start:stop]"""
    if stop - start <= 1: return True
    elif not unico3(S, start, stop-1): return False
    elif not unico3(S, start+1, stop): return False
    else: return S[start]!=S[stop-1]
    
