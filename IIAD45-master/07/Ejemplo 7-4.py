# Ejemplo 7-4. Implementacion de la clase CircularQueue

class Empty(Exception):
    pass

class CircularQueue:
    """Implementacion de cola usando una lista circular"""
    
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
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola
        
        Origina una excepcion Empty si la cola es vacia
        """
        if self.is_empty():
            raise Empty('Cola vacia')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -=1
        return oldhead._element
    
    def enqueue(self, e):
        """Agrega un elemento al final de la cola"""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def rotate(self):
        """Rota el elemento del frente al final de la cola"""
        if self._size > 0:
            self._tail = self._tail._next
            