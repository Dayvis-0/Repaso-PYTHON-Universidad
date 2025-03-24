# Ejemplo 8-1. La clase base abstracta Tree

class Tree:
    """Clase base abstracta que representa una arbol"""
    
    #---------------- clase Position anidada ---------------
    class Position:
        """Abstraccion que representa la localizacion de un solo elemento"""
        
        def element(self):
            """Devolver el elemento almacenado en esta Position"""
            raise NotImplementedError('Debe implementarse por subclase')
            
        def __eq__(self, otro):
            """Devuelve True si otro representa la misma localizacion"""
            raise NotImplementedError('Debe implementarse por subclase')
            
        def __ne__(self, otro):
            """Devuelve True si otro no representa la misma localizacion"""
            raise NotImplementedError('Debe implementarse por subclase')
            
    #-- metodos abstractos que las subclases concretas deben soportar ----
    def root(self):
        """Devuelve Position que es la raiz del arbol (o None si es vacio)"""
        raise NotImplementedError('Debe implementarse por subclase')
        
    def parent(self, p):
        """Devuelve Position que es el padre de p (o None si es vacia)"""
        raise NotImplementedError('Debe implementarse por subclase')

    def num_children(self, p):
        """Devuelve el numero de hijos que Position p tiene"""
        raise NotImplementedError('Debe implementarse por subclase')

    def children(self, p):
        """Genera una iteracion de Positions que representan los hijos de p"""
        raise NotImplementedError('Debe implementarse por subclase')
        
    def __len__(self):
        """Devuelve el numero total de elementos en el arbol"""
        raise NotImplementedError('Debe implementarse por subclase')
        
    #----- metodos concretos impelementados en esta clase ---------
    def is_root(self, p):
        """Devuelve True si Position p es la raiz del arbol"""
        return self.root() == p
    
    def is_leaf(self, p):
        """Devuelve True si Position p no tiene un hijo"""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Devuelve True si el arbol esta vacio"""
        return len(self) == 0

