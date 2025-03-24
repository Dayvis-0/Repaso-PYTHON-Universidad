# Implementacion de la clase Circularqueue

class Empty(Exception):
    pass

class CircularQueue:
    """Implementacion de cola usndo una lista circular"""
    
    #----------------- class _Node anidada ---------------------
    class _Node:
        """Clase ligera y no publica para lamacenar un nodo"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            
            self._element = element
            self._next = next

    #---------------- metodos de la cola ------------------------
    def __init__(self):
        """Crear una cola vacia"""
        
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Devuelve el numero de elementos de la cola"""
        
        return self._size
    
    def is_empty(self):
        """Devolver True si la cola esta vacia"""
        
        return self._size == 0
    
    def _esta_vacio(self):
        """Comprobar si la cola esta vacio"""
        
        if self.is_empty():
            raise Empty('La cola esta vacia')
        
    def first(self):
        """Devuelve (pero no remueve) el elemento delante de la cola"""
        
        self._esta_vacio()
        
        head = self._tail._next
        
        return head._element
    
    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola 
        Origina una excepcion Empty si la cola es vacia"""
        
        self._esta_vacio()
        
        oldhead = self._tail._next
        
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
            
        self._size -= 1
        
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
            
    def __str__(self):
        
        self._esta_vacio()
        
        result = []
        current = self._tail._next
        
        for _ in range(self._size):
            result.append(f'[ {current._element} ]')        
            current = current._next
            
        return ' -> '.join(result)
            
col_cir = CircularQueue()

col_cir.enqueue(1)
col_cir.enqueue(2)
col_cir.enqueue(3)

print(col_cir)