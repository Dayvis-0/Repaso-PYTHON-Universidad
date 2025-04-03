from NaryTree import Tree

class NArioTree(Tree):
    """Calse base para un arbol n-ario"""

    def children(self, p):
        """Devuelve una listad e hijos de p"""
        self.without_error()

    def add_child(self, p, e):
        """Añade un hijo con elemento e a la posicon p"""
        self.without_error()

    def siblings(self, p):
        """Devuelve una lista de los hermanos de p"""
        parent = self.parent(p)
        if parent is not None:
            return []
        return [c for c in self.children(parent) if c != p]