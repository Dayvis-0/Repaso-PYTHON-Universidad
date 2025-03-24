# Una clase PriorityQueueBase con una clase anidad item

class PriorityQeueuBase:
    """Clase base abstracta para una cola de prioridad"""

    #--------------------clase anidad _item ---------------------
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value
            
        def __lt__(self, other):
            
            return self._key < other._key

        def __repr__(self):
            
            return '({0},{1})'.format(self._key, self._value)

    #-------------------- funcionalidad publica ---------------------------
    def is_empty(self):
        """Devuelve True si la cola de prioridad esta vacia"""

        return len(self) == 0

    def __len__(self):
        """Devuelve la cantidad de elementos en una cola de prioridad"""

        self._not_imple()
        
        
        self._not_imple()
        
    def add(self, key, value):
        """Add a key-value pair"""
        
        self._not_imple()
    
    def min(self):
        """Devuelve pero no remueve la tupla (k, v) con clase k minima.
        Origina un error si esta vacia"""
        
        self._not_imple()
        
    def remove_min(self):
        """Remueve y devuelve la tupla (k, v) con el minimo valor k.
        Origina un error si esta vacia"""

        self._not_imple()
    
    def _not_imple(self):
        
        raise NotImplementedError('debe ser implementada por la subclase')