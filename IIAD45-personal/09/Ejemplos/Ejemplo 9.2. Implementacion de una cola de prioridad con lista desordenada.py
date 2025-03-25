# UnsortedPriotityQueue.py Una implementacion de una cola de prioridad usando una lista de desordenada

from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList

class Empty(Exception):
    pass

class UnsortedPriorityQueue(PriorityQueueBase):
    """Una cola de prioridad orientada a minimo con una lista desordenada"""

    #---------------------- funciones no publicas ------------------------------
    def _find_min(self):
        """Devuelve la posicion del item con la clase minima"""

        if self.is_empty():
            raise Empty('Cola de prioridad vacia')

        small = self._data.first()
        walk = self._data.after(small)

        while walk is not None:
            if walk.element() < small.element():
                small = walk

            walk = self._data.after(walk)

        return small
    
    #--------------- funciones publicas ---------------------------------
    def __init__(self):
        """Crea una cola de prioridas nueva y vacia"""

        self._data = PositionalList()

    def __len__(self):
        """Devuelve el numero de elementos de una cola de prioridad"""

        return len(self._data)
    
    def add(self, key, value):
        """Adiciona un nuevo par clave, valor"""

        self._data.add_last(self._Item(key, value))

    def min(self):
        """Devuelve una tupla (k, v) con el minimo valor pero no la remueve 
        Origina una excepcion empty"""

        p = self._find_min()
        item = p.element()
        
        return (item._key, item._value)

    def remove_min(self):
        """Remueve y devuelve una tupla (k, v) con el minimo valor k
        Origina un error si esta vacia"""

        p = self._find_min()
        item = self._data.delete(p)

        return (item._key, item._value)

    def __str__(self):
        """Devuelve una representacion en cadena de la cola de prioridad"""
        
        if self.is_empty():
            raise Empty('Cola de prioridad vacia')
        
        return ' <-> '.join(['[' + str(item) + ']' for item in self._data])
    
copi = UnsortedPriorityQueue()        

copi.add(3, 'a')
copi.add(1, 'b')
copi.add(2, 'c')

print(f'\tCola de prioridad con una lista desordenada: \n{copi}')
print(f'\nEl minimo valor es : {copi.min()[0]} y su clave es: {copi.min()[1]}')
print(f'\nRemovideno el minimo: {copi.remove_min()}')
print(f'\n\tCola de prioridad con una lista desordenada despues de eliminar el minimo:\n{copi}')