# Ejemplo 7-6. Una clase base para manejar una lista doblemente enlazada

class _DoublyLinkedBase:
    """Una clase base que representa una lista doblemente enlazada"""

    class _Node:
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Crea una lista vacia"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer 
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        """Devuelve la cantidad de elementos de la lista"""
        return self._size 
    
    def is_empty(self):
        """Devuelve True si la lista esta vacia"""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Agrega un elemento entre dos nodos existentes"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Borrar un nodo no centinel de la lista"""
        predecessor = node._prev 
        successor = node._next 
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element 
        node._prev = node._next = node._element
        