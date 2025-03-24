# Ejemplo 6-3. Funcion que coincide delimitadores en una expresion

from ArrayStack import ArrayStack

def empareja(expr):
    """Devuelve True si los delimitadores coinciden"""
    apertura = '([}'
    cierre = ')]}'
    S = ArrayStack()
    for c in expr:
        if c in apertura:
            S.push(c)
        elif c in cierre:
            if S.is_empty():
                return False
            if cierre.index(c) != apertura.index(S.pop()):
                return False
    return S.is_empty()

