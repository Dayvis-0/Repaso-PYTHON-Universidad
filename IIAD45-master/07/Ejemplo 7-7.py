# Ejemplo 7-7. Implementacion de la clase LinkedDeque

from _DoublyLinkedBase import _DoublyLinkedBase

class Empty(Exception):
    pass

class LinkedDeque(_DoublyLinkedBase):
    """Implementacion de una deque en base a una lista doblemente enlazada"""
    
    def first(self):
        """Devuelve (pero no remueve) el elemento al frente de la deque"""
        if self.is_empty():
            raise Empty("Deque vacia")
        return self._header._next._element
    
    def last(self):
        """Devuelve (pero no remueve) el elemento al final de la deque"""
        if self.is_empty():
            raise Empty("Deque vacia")
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Agregar un elemento al frente de la deque"""
        self._insert_between(e, self._header, self._header._next)
        
    def insert_last(self, e):
        """Agrega un elemento al final de la deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)
        
    def delete_first(self):
        """Remueve y devuelve el elemento del frente de la deque
        
        Origina una excepcion Empty si la deque esta vacia"""
        if self.is_empty():
            raise Empty("Deque vacia")
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remueve y devuevle el elemento del final de la deque
        
        Origina una excepcion Empty si la deque esta vacia"""
        if self.is_empty():
            raise Empty("Deque vacia")
        return self._delete_node(self._trailer._prev)
