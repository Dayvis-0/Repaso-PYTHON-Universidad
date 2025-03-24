# Ejemplo 6-5. Implementacion de una cola en base a un arreglo

class Empty(Exception):  
    pass

class ArrayQueue:
    """Implementacion FIFO de una cola usando una lista"""
    CAPACIDAD_PREDETERMINADA = 10
    
    def __init__(self):
        """Creando una cola vacia"""
        self._data = [None]*self.CAPACIDAD_PREDETERMINADA
        self._size = 0
        self._front =0
        
    def __len__(self):
        """Devuelve la cantidad de elementos en una cola"""
        return self._size
    
    def is_empty(self):
        """Devuelve True si la cola esta vacia"""
        return self._size == 0
    
    def first(self):
        """Devuelve (pero no remueve) el elemento al frente de la cola
        
        Origina una excepcion Empty si la cola esta vacia
        """
        if self.is_empty():
            raise Empty('Cola vacia')
        return self._data[self._front]
    
    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola
        
        Origina una excepcion Empty si la cola es vacia
        """
        if self.is_empty():
            raise Empty('Cola vacia')
        respuesta = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front +1) % len(self._data)
        self._size -= 1
        return respuesta
        
    def enqueue(self, e):
        """Agrega un elemento al final de la cola"""
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        vuelta = (self._front + self._size) % len(self._data)
        self._data[vuelta] = e
        self._size += 1
        
    def _resize(self, cap):
        """Redimensiona a una nueva lista de capacidad >= len(self)"""
        antiguo = self._data
        self._data = [None]*cap
        avance = self._front
        for k in range(self._size):
            self._data[k] = antiguo[avance]
            avance = (1+avance)%len(antiguo)
        self._front = 0