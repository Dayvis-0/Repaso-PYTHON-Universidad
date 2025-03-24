# Ejemplo 7-3. Implementación del ADT cola usando una lista

class Empty(Exception):
    pass

class LinkedQueue:
    """Implementacion de la cola usando una lista simplemente enlazada"""
    
    #-------------------clase _Node anidadada ----------------------
    class _Node:
        """Clase ligera y no publica para almacenar un nodo"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    #------------------- metodos de la pila ----------------------
    def __init__(self):
        """Crear una cola vacia"""
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Devolver el numero de elementos en la cola"""
        return self._size
    
    def is_empty(self):
        """Devolver True si la cola esta vacia"""
        return self._size == 0
    
    def first(self):
        """Devuelve (pero no remueve) el elemento delante de la cola"""
        if self.is_empty():
            raise Empty('Cola vacia')
        return self._head._element
    
    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola
        
        Origina una excepcion Empty si la cola es vacia
        """
        if self.is_empty():
            raise Empty('Cola vacia')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        """Agrega un elemento al final de la cola"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        