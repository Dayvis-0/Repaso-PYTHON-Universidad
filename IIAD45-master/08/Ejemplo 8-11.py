# Ejemplo 8-11. Soporte para realizar un recorrido postorden de un arbol

def postorder(self):
    """Genera una iteracion postorden de posiciones en el arbol"""
    if not self.is_empty():
        for p in self._subtree_postorder(self.root()):
            yield p
            
def _subtree_postorder(self, p):
    """Genera una iteracion postorden de posiciones en el arbol con raiz en p"""
    for c in self.children(p):
        for other in self._subtree_postorder(c):
            yield other
    yield p