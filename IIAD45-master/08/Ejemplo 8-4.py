# Ejemplo 8-4. Metodo _height2 de la clase Tree

def _height2(self, p):
    """Devuelve la altura del subarbol con raiz en la posicion p"""
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.children(p))

