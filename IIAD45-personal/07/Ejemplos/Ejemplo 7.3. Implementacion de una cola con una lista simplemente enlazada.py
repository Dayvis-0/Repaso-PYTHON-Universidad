# Implementacion del ADT cola usando una lista simplemente enlazada

#from Empty import Empty
class Empty(Exception):
    pass

class LinkedQueue:
    """Implementacion de la cola usando una lista simplemente enlazada"""
    
    #------------------------ clase _Node anidada -----------------------
    class _Node:
        """Clase ligera y no publica para almacenar un nodo"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element 
            self._next = next
            
    #----------------------- metodos de la cola -----------------------
    def __init__(self):
        """Crear una cola vacia"""
        
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Devuelve el numero de elementos que hay en la cola"""
        
        return self._size
    
    def is_empty(self):
        """Devuelve true si la cola esta vacia"""
        
        return self._size == 0
    
    def _esta_vacio(self):
        
        if self.is_empty():
            raise Empty('Cola vacia')
        
    def first(self):
        """Devuelve (pero no remueve) el elemento delante de la cola"""
        
        self._esta_vacio()
        
        return self._head._element
    
    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola
        Origina una excepcion Empty si la coola esta vacia"""
        
        self._esta_vacio()
        
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
        
    def __str__(self):
        
        self._esta_vacio()
        
        result  = []
        current = self._head
        
        while current:
            result.append(f'[ {current._element} ]')
            current = current._next
        
        return ' -> '.join(result)
        
co_li = LinkedQueue()

co_li.enqueue(1)
co_li.enqueue(2)
co_li.enqueue(3)

print(co_li)