# Ejemplo 8-8. Iterando todos los elementos de una instancia de Tree

def __iter__(self):
    """Genera una iteracion de los elementos del arbol"""
    for p in self.positions():
        yield p.element()