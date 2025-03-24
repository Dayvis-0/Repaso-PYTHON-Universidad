# La clase base abstracta Tree

class Tree:
    """Abstraccion que representa la localizacion de un solo elemento"""
    
    #---------------------clase Position anidada ----------------------
    class Position:

        def element(self):
            """Devuelve el elementto almacenado en esta posicion"""

            self._without_error()
        
        def __eq___(self):
            """Devvuelve True si otro representa la misma localizacion"""

            self._without_error()
        
        def __ne__(self):
            """Devuelve Ttrue si otro no representa la misma localizacion"""

            self._without_error()

        def _without_error(self):
            
            raise NotImplementedError('Debe implementarse por sublcase')

    #---metodos abstractos que las subclases concretas deben soportar -----
    def root(self):
        """Devuelve Positon que la raiz del arbol (o None si es vacio)"""
        
        self._without_error()
        
    def parent(self, p):
        """Devuelve Position que es el padre de pp (o None si es vacio)"""

        self._without_error()
    
    def num_children(self, p):
        """Devuelve el numero de hijos que Position tiene"""

        self._without_error()
    
    def children(self, p):
        """Genera una iteracion Position que representan los hijos de p"""

        self._without_error()
    
    def __len__(self):
        """Devuelve el numero total de elementos en el arbol"""

        self._without_error()

    def _without_error(self):
    
        raise NotImplementedError('Debe implementarse por sublcase')

    #¿------ Metodos concretos implementados en esta clase -------------
    def is_root(self, p):
        """Devuelve True si Position p es la raiz del arbol"""        

        return self.root() == p
    
    def is_leaf(self, p):
        """Devuelve True si Position p no tiene un hijo"""

        return self.num_children(p) == 0
    
    def is_empty(self):
        """Devuelve True si el arbol esta vacio"""
        
        return len(self) == 0
    
    #-------- Metodos ----------
    def depth(self, p):
        """Devuelve el numero de niveles separando posciones P desde la raiz"""

        if self.is_root(p):
            return 0
        else: 
            return 1 + self.depth(self.parent(p))
        
    def _height(self):
        """Devuelve la altura del arbol"""

        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _height2(self, p):
        """Devuelve la altura del subarbol  con raiz en la posicion p"""

        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        """Devuelve la altura del subarbol con raiz en la posicion p
        si p es None, devuelve la altura del arbol entero"""

        if p is None:
            p = self.root()
        
        return self._height2(p)