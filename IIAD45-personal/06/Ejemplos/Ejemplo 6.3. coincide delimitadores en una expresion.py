# Funcion para emparejar delimitadores en expresiones aritmeticas

from ArrayStack import ArrayStack

def empareja(expresion):
    """Devuelve True si los delimitadores coinciden"""
    
    apertura = '([{'
    cierre = ')]}'
    
    S = ArrayStack()
    
    for c in expresion:
        
        if c in apertura:
            S.push(c)
        
        elif c in cierre:
            
            if S.is_empty():
        
                return False

            if cierre.index(c) != apertura.index(S.pop()):
                
                return False

    return S.is_empty()       

if empareja('(2+2)'):
    print('Los delimitadores coinciden')

else:
    print('Los delimitadores no coinciden')