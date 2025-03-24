# Ejemplo 5-3. Midiendo el costo de append

from time import time
def calcula_promedio(n):
    """Ejecuta n appends y devuelve el tiempo promedio"""
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start)/n
