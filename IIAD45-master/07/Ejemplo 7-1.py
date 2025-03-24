# Ejemplo 7-1. Una clase ligera _Nodo

class _Node:
    """Clase ligera y no publica para almacenar un nodo"""
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next

