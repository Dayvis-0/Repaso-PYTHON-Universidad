# Ejemplo 8-3. Metodo _height1 de la clase Tree

def _height1(self):
    """Devuelve la altura del arbol"""
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

