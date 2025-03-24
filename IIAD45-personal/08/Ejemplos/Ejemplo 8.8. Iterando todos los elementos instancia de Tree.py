# Iterando todos los elementos de una instancia de Tree

def __iter__(self):
    """genera una iteracion de los elementos del arbol"""

    for p in self.positions():
        
        yield p.element()