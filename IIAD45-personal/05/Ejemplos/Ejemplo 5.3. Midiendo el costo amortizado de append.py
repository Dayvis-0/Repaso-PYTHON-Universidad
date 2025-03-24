# Midiendo el costo amoritizado de append

from time import time

def calcula_promedio(n):
    """Ejecuta n appends y develve el tiempo promedio"""
    
    data = []
    start = time()
    
    for i in range(n):
        data.append(None)
        
    end = time()
    
    return (end - start)/n


print(calcula_promedio(1000000))