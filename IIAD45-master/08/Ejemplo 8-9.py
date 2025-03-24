# Ejemplo 8-9. Soporte para realizar una recorrido preorden de un arbol debe ser incluido en el curpo de la clase Tree

def preorder(self):
    """Genera una iteracion preorden de posiciones en el arbol"""
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()):
            yield p
            
def _subtree_preorder(self, p):
    """Genera una iteracion preorden de posiciones en el arbol con raiz en p"""
    yield p
    for c in self.children(p):
        for other in self._subtree_preorder(c):
            yield other