# Metodo publico Tree.height que calcula la altura del arbol entero

def heigh1(self, p=None):
    """Devuelve la altura del subarbol con raiz en la posicion p
    ssi p es None, devuelve altura del arbol entero"""

    if p is None:
        p = self.root()
        
    return self._height2(p)