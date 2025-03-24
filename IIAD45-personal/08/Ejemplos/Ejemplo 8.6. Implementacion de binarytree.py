# Una clase abstracta BinaryTree que extiende la clase Tree

from Tree import Tree

class BinaryTree(Tree):
    """Clase base abstracta que representa un arbol binario"""

    #---------------- metodos adicionales abstractos --------------
    def left(self, p):
        """Devuelve una posicion representado el hijo de p
        Devuelve None si p no tiene un hijo izquierdo"""

        self.without_error()
        
    def right(self, p):
        """Devuelve una posicion que representa el hijo derecho 
        Devuelve None si p no tiene un hijo derecho"""
        
        self.without_error()

    #--------- metodos concretos implementados en la clase ------------
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
        """"Generar una iteracion de posiciones representando hijos"""

        if self.left(p) is not None:
            
            yield self.left(p)

        if self.right(p) is not None:
            
            yield self.right(p)