# Implementacion de una pila usando una lista
# LIFO (LLast input, first output) - (Ultimo en entrar, primero en salir)

class Empty(Exception):
    
    pass

class ArrayStack:
    """imlementacion deuna pila usando una lista"""
    
    def __init__(self):
        """Creando una pila vacia"""
        
        self._data = []
        
    def __Len__(self):
        """Devuelve la cantidad de elementos de la pila"""
        
        return len(self._data)
    
    def is_empty(self):
        """Devuelve True si la pila esta vacia"""
        
        return len(self._data) == 0
    
    def push(self, e):
        """Agrega el elemento e a la classe de la pila"""
        
        self._data.append(e)
        
    def _vacio(self):
        
        if self.is_empty():
            raise Empty('Pila vacia')
        
    def top(self):
        """Devuelve (peron no remueve) el elemento en la scima de la pila
        Origina una excepcion si la pila esta vacia"""
        
        self._vacio()
        
        return self._data[-1]
    
    def pop(self):
        """Remueve y devuelve el elemento de la cima de la pila
        origina un excepcion si la pila esta vacia"""
        
        self._vacio()
        
        return self._data.pop()
    
    def __str__(self):
        
        return str([j for j in self._data])   

pila = ArrayStack()

pila.push(1)
pila.push(2)
pila.push(3)

print(pila)

pila.pop()

print(pila)