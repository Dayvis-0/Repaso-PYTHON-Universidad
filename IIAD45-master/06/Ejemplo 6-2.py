# Ejemplo 6-2. una función que revierte el orden de las lineas de un archivo

from ArrayStack import ArrayStack

def revertir_archivo(archivo):
    """Sobreescribe el archivo con su contenido revertido"""
    S = ArrayStack()
    original = open(archivo)
    for linea in original:
        S.push(linea.rstrip('\n'))
    original.close()
    
    salida = open(archivo, 'w')
    while not S.is_empty():
        salida.write(S.pop() + '\n')
    salida.close()

revertir_archivo("archivo.txt")