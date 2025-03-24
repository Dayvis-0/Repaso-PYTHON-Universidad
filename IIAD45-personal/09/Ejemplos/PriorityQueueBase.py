class PriorityQueueBase:
    
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value
            
        def __lt__(self, other):
            
            return self._key < other._key

        def __repr__(self): 
            
            return '({0},{1})'.format(self._key, self._value)

    def is_empty(self):
        
        return len(self) == 0
    
    def __len__(self):
        
        self._not_imple()

    def min(self):
        
        self._not_imple()

    def remove_min(self):
        
        self._not_imple()
    
    def _not_imple(self):
        
        raise NotImplementedError('debe ser implementada por la subclase')