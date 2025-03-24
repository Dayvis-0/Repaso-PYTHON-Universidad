# Ejemplo 8-13. Soporte para realizar un recorrido inorden en un arbol binario

def inorder(self):
    """Generar una iteracio inorden de posicoines en el arbol"""
    if not self.is_empty():
        for p in self._subtree_inorder(self.root()):
            yield p
            
def _subtree_inorder(self, p):
    """Genera una iteracion inorden de posiciones en un subarbol etiquetado como p."""
    if self.left(p) is not None:
        for other in self._subtree_inorder(self.left(p)):
            yield other
    yield p
    if self.right(p) is not None:
        for other in self._subtree_inorder(self.right(p)):
            yield other
