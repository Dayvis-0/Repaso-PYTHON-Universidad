# Implementacion del ADT pila usando una lista simplemente enlazada

from Empty import Empty

class LinkedStack:
    """Implementacion de pila usando una lista simplemente enlzada"""
    
    #------------------------ clase _Node anidada -------------------
    class _Node:
        """Clase ligera y no publica para almacenar un nodo"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    #------------------------- metodo de la pila -------------------
    def __init__(self):
        """Crear una pila vacia"""
        self._head = None
        self._size = 0
        
    def __len__(self):
        """Devolver el numero de elementos en la pila"""
        
        return self._size
    
    def is_empty(self):
        """Devuelve true si la pila esta vacia"""
        
        return self._size == 0
    
    def _esta_vacio(self):
        
        if self.is_empty():
            raise Empty('Pila vacia')        

    def push(self, e):
        """Agregar el elemento e a la cima de la pila"""
        
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def top(self):
        """Devolver (pero no remover) el elemento en la cima
        Origina Empty si la pila esta vacia"""
        
        self._esta_vacio()
        
        return self._head._element
    
    def pop(self):
        """Remueve y devuelve el elemento de la cima de la pila
        Origina un exception Empty si la pila esta vacia"""
        
        self._esta_vacio()
        
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        return answer
    
    def __str__(self):
        
        self._esta_vacio()
        
        result = []
        current = self._head
        
        while current:
            result.append(f'[ {current._element} ]')
            current = current._next

        return " -> ".join(result)
    
li_en = LinkedStack()

li_en.push(1)
li_en.push(2)
li_en.push(3)
print(li_en)

li_en.push(4)
li_en.push(5)
li_en.push(6)

print(li_en)

print('Eliminado', li_en.pop())

print(li_en)