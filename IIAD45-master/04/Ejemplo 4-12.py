# Ejemplo 4-12. Sumando los elementos de una secuencia usando recursividad binaria

def suma_binaria(S, start, stop):
    """Devuelve la suma de los numeros en el slice S[start:stop]"""
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return suma_binaria(S, start, mid) + suma_binaria(S, mid, stop)