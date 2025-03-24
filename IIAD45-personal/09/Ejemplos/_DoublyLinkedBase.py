class _DoublyLinkedBase:
    """Una clase base que representa una lista doblemente enlazada"""

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
    def __init__(self):
        """Crear una lista vacia"""

        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self): 
        """Devuelve la cantidad de elementos de la lista"""

        return self._size
    
    def is_enmpty(self):
        """Devueve True si la lista esta vacia"""

        return self._size == 0
    
    def _insert_between(self, e, predecesor, sucesor):
        """Agrega un elemento entre dos nodos existentes"""
        
        newest = self._Node(e, predecesor, sucesor)
        predecesor._next = newest
        sucesor._prev = newest
        self._size += 1
        
        return newest
    
    def _delete_node(self, node):
        """Borra un nodo no centinel de la lista"""

        predecesor = node._prev
        sucesor = node._next
        predecesor._next = sucesor
        sucesor._prev = predecesor
        self._size -= 1 
        element = node._element
        node._prev = node._next = None
        
        return element