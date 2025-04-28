class Emty(Exception):
    pass
    
class ArrayStack:
    
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_emty(self):
        return len(self._data)  == 0

    def push(self, e):
        self._data.append(e)

    def _vacio(self):
        
        if self.is_emty():
            raise Emty("Pila vacia")
        
    def top(self):
        self._vacio()
        return self._data[-1]

    def pop(self):
        self._vacio()
        return self._data.pop()

    def __str__(self):
        
        return str([j for j in self._data])