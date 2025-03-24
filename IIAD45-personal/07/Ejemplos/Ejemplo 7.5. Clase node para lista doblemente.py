# Una clase _Node par el uso de una lista doblemente enlazada 

class _Node:
    """Clase no publica para almacenar un nodo de llista doblemente enlazada"""
    __slots__ = '_element', '_prev', '_next'
    
    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next