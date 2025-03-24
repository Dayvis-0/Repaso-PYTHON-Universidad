# Ejemplo 6-1. Implementa una pila usando una lista

#ArrayStack.py
class Empty(Exception):  
    pass

class ArrayStack:
    """Implementacion de una pila usando una lista"""
    
    def __init__(self):
        """Crea una pila vacia"""
        self._data = []
        
    def __len__(self):
        """Devolver la cantidad de elementos en la pila"""
        return len(self._data)
    
    def is_empty(self):
        """Devuelve True si la pila esta vacia"""
        return len(self._data) == 0
    
    def push(self, e):
        """Agrega el elemento e a la cima de la pila"""
        self._data.append(e)
        
    def top(self):
        """Devuelve (pero no remueve) el elemento en la cima de la pila
        
        Origina una excepcion si la pila esta vacia"""
        if self.is_empty():
            raise Empty('Pila vacia')
        return self._data[-1]
    
    def pop(self):
        """Remueve y devuelve el elemento de la cima de la pila
        
        Origina una excepcion si la pila esta vacia"""
        if self.is_empty():
            raise Empty('Pila vacia')
        return self._data.pop()
    
    
        