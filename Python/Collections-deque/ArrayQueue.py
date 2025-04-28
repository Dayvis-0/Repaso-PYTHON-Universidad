class Empty(Exception):
    pass

class ArrayQueue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def _vacio(self):
        if self.is_empty():
            raise Empty("Cola vacia")
        
    def first(self):
        self._vacio()
        return self._data[0]

    def dequeue(self):
        return self._data[0]
    
    def enqueue(self, e):
        self._data.append(e)

    def __str__(self):
        
        return str([j for j in self._data])

col1 = ArrayQueue()

col1.enqueue(1)
col1.enqueue(2)
col1.enqueue(3)

print(col1)
print(col1.dequeue())