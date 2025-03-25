from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList

class Empty(Exception):
    pass

class UnsortedPriorityQueue(PriorityQueueBase):
    
    def _find_min(self):
        
        if self.is_empty():
            raise Empty('Cola de prioridad vacia')

        small = self._data.firt()
        walk = self._data.after(small)

        while walk is not None:
            if walk.element() < small.element():
                small = walk
                
            walk = self._data.after(walk)

        return small
    
    def __init__(self):
        
        self._data = PositionalList()

    def __len__(self):
        
        return len(self._data)

    def add(self, key, value):
        
        self._data.add_last(self._Item(key, value))

    def min(self):
        
        p = self._find_min()
        item = p.element()

        return (item._key, item._value)

    def remove_min(self):
        
        p = self._find_min()
        item = p.element()
        self._data.delete(p)

        return (item._key, item._value)