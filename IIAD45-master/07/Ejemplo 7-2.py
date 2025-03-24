# Ejemplo 7-2. Implementación del ADT pila usando una lista

class Empty(Exception):
    pass

class LinkedStack:
    """Implementacion de pila usando una lista simplemente enlazada"""
    
    #-------------------clase _Node anidadada ----------------------
    class _Node:
        """Clase ligera y no publica para almacenar un nodo"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    #------------------- metodos de la pila ----------------------
    def __init__(self):
        """Crear una pila vacia"""
        self._head = None
        self._size = 0
        
    def __len__(self):
        """Devolver el numero de elementos en la pila"""
        return self._size
    
    def is_empty(self):
        """Devolver True si la pila esta vacia"""
        return self._size == 0
    
    def push(self, e):
        """Agregar el elemento e a la cima de la pila"""
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def top(self):
        """Devolver (pero no remover) el elemento en la cima
        
        Origina Empty si la pila esta vacia
        """
        if self.is_empty():
            raise Empty('Pila vacia')
        return self._head._element
    
    def pop(self):
        """Remueve y devuelve el elemento de la cima de la pila
        
        Origina una excepcion Empty si la pila esta vacia
        """
        if self.is_empty():
            raise Empty('Pila vacia')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
