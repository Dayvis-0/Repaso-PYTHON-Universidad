# Ejemplo 3-1.  Funcion que devuelve el mayor valor de una lista

def encontrar_maximo(data):
    """Devuelve el elemento maximo de una lista"""
    masgrande = data[0]
    for val in data:
        if val > masgrande:
            masgrande = val
    return masgrande
