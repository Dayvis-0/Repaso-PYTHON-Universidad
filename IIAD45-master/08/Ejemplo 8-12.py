# Ejemplo 8-12. Una implementacion del recorrido primero en amplitud

from LinkedQueue import LinkedQueue

def breadhfirst(self):
    """Genera una iteracion primero en amplitud de las posiciones del arbol"""
    if not self.is_empty():
        fringe = LinkedQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            for c in self.children(p):
                fringe.enqueue(c)
