# Ejemplo 4-2. Implementacion recursiva de la regal inglesa

def dibujar_linea(longitud_marca, etiqueta=''):
    """Dibujar una linea con una longitu dada de marca"""
    linea = '-'*longitud_marca
    if etiqueta:
        linea += ' ' + etiqueta
    print(linea)
    
def dibujar_intervalo(longitud_centro):
    """Dibuja la marca de intervalo en base a la longitud de la marca central"""
    if longitud_centro > 0:
        dibujar_intervalo(longitud_centro - 1)
        dibujar_linea(longitud_centro)
        dibujar_intervalo(longitud_centro -1)
        
def dibujar_regla(num_pulgadas, longitud_mayor):
    "Dibuja una regla inglesa con un numero dado de pulgadas"""
    dibujar_linea(longitud_mayor, 'O')
    for j in range(1, 1 + num_pulgadas):
        dibujar_intervalo(longitud_mayor - 1)
        dibujar_linea(longitud_mayor, str(j))
