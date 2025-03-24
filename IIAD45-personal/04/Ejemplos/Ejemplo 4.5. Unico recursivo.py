def unico3(S, start, stop):
    """Devuelve True si no hay elementos duplicados eb el slice [start:stop]"""
    
    if stop - start <= 1: return True
    elif not unico3(S, start, stop - 1): return False
    elif not unico3(S, start + 1, stop): return False
    else: return S[start] != S[stop-1]
    
nume = [1,3,3]


if unico3(nume, 0, len(nume)):
    print('No hay numeros repetidos')

else:
    print('Hay numeros repetidos')
