class Empty(Exception):
    pass

class _DoubleLinkedBase:
    
    class _Node: 
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next       
        
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        
        self._header._next = self._trailer
        self._trailer._prev = self._header
        
        self._size = 0
        
    def __len__(self):
        
        return self._size
    
    def is_empty(self):
        
        return self._size == 0
    
    def _check_empty(self):
        
        if self.is_empty():
            Empty('La lista doblemente enlazada esta vacia')
            
    def _insert_betweeen(self, e, predecesor, sucesor):
        newest = self._Node(e, predecesor, sucesor)
        predecesor._next = newest
        sucesor._prev = newest
        self._size += 1
        
        return newest 
    
    def _delete_node(self, node):
        predecesor = node._prev
        sucesor = node._next
        
        predecesor._next = sucesor
        sucesor._prev = predecesor
        
        self._size -= 1
        element = node._element
        node._prev = node._next = None
        
        return element