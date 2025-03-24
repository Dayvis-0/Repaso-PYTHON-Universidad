# Implementacion recursiva de la regla inglesa

def dibujar_linea(longitud_marca, etiqueta = ''):
    """Dibujar una linea con una longitud dada marca"""
    
    linea = '-' * longitud_marca
    
    if etiqueta:
        linea += ' ' + etiqueta
        
    print(linea)
    
def dibujar_intervalo(longitud_centro):
    """Dibujar la marca de intervalo en base a la longitud de la marca central"""
    
    if longitud_centro > 0:
        dibujar_intervalo(longitud_centro - 1)
        dibujar_linea(longitud_centro)
        dibujar_intervalo(longitud_centro - 1)
        
def dibujar_regla(num_pul, long_mayor):
    """Dibuja una regla inglesa con un numero dado de pulgadas"""

    dibujar_linea(long_mayor, '0')
    
    for i in range(1, 1 + num_pul):
        dibujar_intervalo(long_mayor - 1)
        dibujar_linea(long_mayor, str(i))
        
dibujar_regla(2,3)