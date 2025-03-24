# Ejemplo 8-6. La clase BinaryTree en base a la clase Tree

from Tree import Tree 

class BinaryTree(Tree):
    """Clase base abstracta que representa un arbol binario"""
    
    # ---------------- metodos adicionales abstractos ----------------
    def left(self, p):
        """Devuelve una posicion representado el hijo de p
        
        Devuelve None si p no tiene un hijo izquierdo
        """
        raise NotImplementedError('debe ser implementado por la subclase')
        
    def right(self, p):
        """Devolver una posicion que representa el hijo derecho
        
        Devuelve None si p no tiene un hijo derecho
        """
        raise NotImplementedError('debe ser implementdo por la sublcase')
        
    # ----------- metodos concretos implementados en la ca clase -----
    def sibling(self, p):
        """Devuelve una posicion que representa el hermano de p"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self, p):
        """Generar una iteracion de posiciones representando hijos"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            
    
        

