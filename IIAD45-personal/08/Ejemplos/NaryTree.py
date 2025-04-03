class Tree:
    """Clase base abstracta que representa un arbol n-ario"""

    class Position:
        """Abstraccion que representa la localizacion de un solo elemento"""

        def element(self):
            """Devuelve el elemento almacenado en eta Posicion"""
            self.without_error()

        def __eq__(self):
            """Devuelve True si otro presenta la misma localizacion"""
            self.without_error()
        
        def __ne__(self):
            """Devuelve True si otro no representa la misma localizacion"""
            self.without_error()

        def without_error():
            raise NotImplementedError("Debe imlementarse para subclase")

    #Todo Metodos abstractos que las subclases concretas deben soportar
    def root(self):
        """Devuelve Position que es la raiz del arbol (o None si esta vacio)"""
        self.whithout_error()

    def parent(self, p):
        """Devuelve Position que es el padre de p (O none si esta vacio)"""
        self.without_error()

    def num_children(self, p):
        """Devuelve el numero de hijos que tiene la posicon p"""
        self.without_error()
    
    def children(self, p):
        """Genera una iteracion de Positions que representan llos hijos p"""
        self.without_error()

    def __len__(self):
        """Devuevle el numero total de elementos en el arbol"""
        self.without_error()

    def without_error(self):
        raise NotImplementedError("Debe implementarse para subclase")
    
    #todo Metodos concretos implementados en esta clase
    def is_root(self, p):
        """Devuelve True si Position p es la raiz del arbol"""
        return self.root() == p

    def is_leaf(self, p):
        """Devuelve True si Position p no tiene hijos"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Devuelve True si el arbol esta vacio"""
        return len(self) == 0

    def depth(self, p):
        """Devuelve el numero de niveles separando la posicion p desde la raiz"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def height(self, p=None):
        """Devuelve la altura del subarbol con raiz en la posicion p
        Si p e None, devuelve la altura del arbol entero"""
        if p is None:
            p = self.root()
        return self._hight2(p)
    
    def _height2(self, p):
        """Devuelve la altura del subarbol con raiz en la posicion p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def __iter__(self):
        """Genera una iteracion de los elementos del arbol"""
        for p in self.positions():
            yield p.element()
        
    def preorden(self):
        """Genera una iteracion preorden de posiciones en el arbol"""
        if not self.is_empty():
            for p in self._subtree_preorder(self, p):
                yield p
                
    def _subtree_preorder(self, p):
        """Genera una iteracion prorden de posiciones en el subarbol con raiz en p"""
        yield p
        for c in self.children(p):
                yield from self._subtree_preorder(c)

    def positions(self):
        """Genera una iteracion de las posiciones del arbol"""
        return self.preorden()