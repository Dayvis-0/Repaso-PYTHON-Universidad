# Implementacion de clase LinkedDeque

from _DoubleLinkedBase import _DoubleLinkedBase

class LinkedDeque(_DoubleLinkedBase):
    """Implementacion de una deque en base a una lista doblemente enlazada"""
    
    def first(self):
        """Devuelve (pero no remueve) el elemnto al frende de la deque"""
    
        self._check_empty()
        
        return self._header._next._element
    
    def last(self):
        """Devuelve (pero no remueve) el elemento al final de la deque"""
        
        self._check_empty()
        
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Agregar un elemento al frente de la deque"""
        
        self._insert_betweeen(e,self._header, self._header._next)
        
    def insert_last(self, e):
        """Agrega un elemento al final de la deque"""
        
        self._insert_betweeen(e, self._trailer._prev, self._trailer)
        
    def delete_first(self):
        """Remueve y devuelve el elemento del frente de la deque
        Origina una excepcion Empty si la deque esta vacia"""
        
        self._check_empty()
        
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remueve y devuelve el elemento del final de la deque
        Origina una excepcion Empty si la deque esta vacia"""
        
        self._check_empty()
        
        return self._delete_node(self._trailer._prev)
    
    def __str__(self):
        
        resu = []
        
        current = self._header._next
        
        while current is not self._trailer:
            
            resu.append(f'[ {current._element} ]')
            current = current._next

        return '<->'.join(resu)

ld1 = LinkedDeque()

ld1.insert_first(1)
ld1.insert_first(2)

print(ld1)

ld1.insert_last(4)
ld1.insert_last(5)

print(ld1)

print(ld1.delete_first())

print(ld1)

print(ld1.delete_last())

print(ld1)