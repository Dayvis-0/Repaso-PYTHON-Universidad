# Metodo _height1 de la clase Tree

def _height(self):
    """Devuelve la altura del arbol"""

    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    