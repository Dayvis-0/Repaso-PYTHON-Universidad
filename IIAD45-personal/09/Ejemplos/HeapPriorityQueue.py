from PriorityQueueBase import PriorityQueueBase

class Empty(Exception):
    pass

class HeapPriorityQueue(PriorityQueueBase): # La clase base define -Item
    """Una cola de prioridad orientada a min implementada con un montón binario"""

    #---------------------- monpublic behaviors --------------------
    def _parent(self, j):
        
        return (j - 1) // 2

    def _left(self, j):
        
        return 2*j + 1
    
    def _right(self, j):
        
        return 2*j + 2

    def _has_left(self, j):
        
        return self._left(j) < len(self._data) # index beyond end of list?
    
    def _has_right(self, j):
        
        return self._right(j) < len(self._data) # index beyond end of list?
    
    def _swap(self, i, j):
        """Intercambia los elementos en los índices i y j de la matriz"""
        
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        
        parent = self._parent(j)

        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # repetirse en la posición del padre
        
    def _downheap(self, j):
        
        if self._has_left(j):
            left = self._left(j)
            small_child = left # Aunque la derecha puede ser más pequeña

            if self._has_right(j):
                right = self._right(j)
                
                if self._data[right] < self._data[left]:
                    small_child = right
                
                if self._data[small_child] < self._data[j]:
                    self._swap(j, small_child)
                    self._downheap(small_child) # volver a aparecer en la posición del niño pequeño
          
    #----------------------- comportamientos públicos -------------------          
    def __init__(self):
        """Crar un nueva Pila de Prioridad vacia """

        self._data = []

    def __len__(self):
        """Devuelve el numero del elementos en la cola de prioridad"""
        
        return len(self._data)
    
    def add(self, key, value):
        """Agrega un par clave-valor a la cola de prioridad"""

        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1) # Posicion recien añadida
    
    def min(self):
        """Devuelve, pero no elimina la tupla (k, v) con el minimo clave.
        Genera un excepcion Empty si esta vacio"""

        self._check_empty()
        
        item = self._data[0]

        return (item._key, item._value)
            
    def remove_min(self):
        """Elimina y devuelve la tupla (k, v) con el minimo clave
        Genera una excepcion Empty si esta vacia"""

        self._check_empty()

        self._swap(0, len(self._data - 1))
        item = self._data.pop()
        self._downheap(0)

        return (item._key, item._value)
            
    def _check_empty(self):
        
        if self.is_empty():
            raise Empty('La Cola de Prioridad esta vacia')