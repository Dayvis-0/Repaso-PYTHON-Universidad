# Una clase base para mejorar una lista doblemente enlazada

class Empty(Exception):
    pass

class _DoubleLinkedBase:
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

    def is_empty(self):
        """Devuelve True si la lista esta vacia"""

        return self._size == 0
    
    def _check_empty(self):
        
        if self.is_empty():
            Empty('La lista esta vacia')
            
    def _insert_between(self, e, predecesor, sucesor):
        """Agregar un elemento entre dos nodos existentes"""
        
        newest = self._Node(e, predecesor, sucesor)
        
        predecesor._next = newest
        sucesor._prev = newest
        self._size += 1
        
        return newest
    
    def _delete_node(self, node):
        """Borrar un nodo no centinela de la lista y devuelve su elemento"""
        
        predecesor = node._prev
        sucesor = node._next
        
        predecesor._next = sucesor
        sucesor._prev = predecesor
        self._size -= 1
        
        element = node._element
        node._prev = node._next = None
        
        return element
    
    def add_first(self, e):
        """Agregar un elemento al principio de la lista"""
        
        self._insert_between(e, self._header, self._header._next)
        
    def add_last(self, e):
        """Agrega un elemento al final de la lista"""
        
        self._insert_between(e, self._trailer._prev, self._trailer)
        
    def delete_firt(self):
        """Eliminar el primer elemento de la lista y devolverlo"""
        
        self._check_empty()
        
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Eliminar el ultimo elemento de la lista y devlverlo"""
        
        self._check_empty()
        
        return self._delete_node(self._trailer._prev)
    
    def __str__(self):
        """Mostrar la lista con flechas indicando la conexión entre nodos"""

        if self.is_empty():
            return "Lista vacía"
        
        result = []
        current = self._header._next
        
        while current is not self._trailer:
            result.append(f"[ {current._element} ]")  # Formato de cada nodo
            current = current._next
        
        return " <-> ".join(result)
    
doble = _DoubleLinkedBase()

doble.add_first(1)
doble.add_first(2)

print(doble)