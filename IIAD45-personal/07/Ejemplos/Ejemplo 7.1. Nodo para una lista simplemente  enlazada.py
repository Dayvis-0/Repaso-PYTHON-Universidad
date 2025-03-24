# Una clase _Nodo para una lista simplemente enlazada

class _Node:
    """Clase ligera y no publica pra almacenar un nodo"""
    
    __slots__ = '_element','_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        