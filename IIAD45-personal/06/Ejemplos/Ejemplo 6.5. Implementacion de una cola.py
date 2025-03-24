# Implementacion basada en arreglo de una cola
# FIFO (first input, first output) - (primeor en entrar, primero en salir)

class Empty(Exception):
    pass

class ArrayQueue:
    """Implementacion FIFO de una cola usando una lista"""
    capacidad_preterminada = 10
    
    def __init__(self):
        """Creando una cola vacia"""
        
        self._data = [None]*self.capacidad_preterminada
        self._size = 0
        self._front = 0 
        
    def __len__(self):
        """Devuelve la cantidad de elementos de una cola"""
        
        return self._size
    
    def is_empty(self):
        """Devuelve true si la cola esta vacia"""
        
        return self._size == 0
    
    def _esta_vacio(self):
    
        if self.is_empty():
            raise Empty('Cola vacia')
    
    def first(self):
        """Devuelve (pero no remueve) el elemento al frente de la cola
        Origina una excepcion Empty si la cola esta vacia"""
        
        self._esta_vacio()
        
        return self._data[self._front]
    
    def dequeue(self):
        """Remueve y devuelve el primer elemento de la cola
        Origina una excepcion Empty si la cola es vacia"""
        
        self._esta_vacio()
        
        respuesta = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        
        return respuesta
    
    def enqueue(self,e):
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
        
        for j in range(self._size):
            self._data[j] = antiguo[avance]
            avance = (1+avance) % len(antiguo)
            
        self._front = 0

    def __str__(self):
        return str([self._data[(self._front + j) % len(self._data)] for j in range(self._size)])

        
col = ArrayQueue()

col.enqueue(1)
col.enqueue(2)
col.enqueue(3)

print(col)

print(col.dequeue())

print(col)