# Funcion recursiva para reportar el uso del disco

import os

def uso_disco(path):
    """Devuelve el numero de bytes usados por un directorio y sus decendientes"""
    
    total = os.path.getsize(path)
    
    if os.path.isdir(path):
        
        for filename in os.listdir(path):
            
            childpath = os.path.join(path, filename)
            total += uso_disco(childpath)
            
    return total

print(uso_disco(r'C:\Users\ASUS I5\Music'))