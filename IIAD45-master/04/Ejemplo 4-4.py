# Ejemplo 4-4. Una funcion recursiva para reporta el uso de disco

import os

def uso_disco(path):
    """Devuelve el numero de bytes usados por un directorio y sus descencientes"""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += uso_disco(childpath)
            
    #print('{0:<7}'.format(total), path)
    return total
    