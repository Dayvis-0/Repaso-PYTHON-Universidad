# Sumando los elementos de una secuencia usando recursividad

def suma_binaria(S, start, stop):
    """Devuelve lla suma de los numeros en el slice S[start:stop]"""
    
    if start >= stop:
    
        return 0

    elif start == stop - 1:
        
        return S[start]
    
    else:
        
        mid = (start + stop) // 2
        
        return suma_binaria(S, start, mid) + suma_binaria(S, mid, stop)
    
nume = [1,2]

print(suma_binaria(nume, 0, len(nume)))