class Tree:
    """Clase base abstracta que representa un arbol"""

    #---------clase Position anidada--------
    class Position:
        """Abstraccion que representa la localizacion de un solo elemento"""
        
        def element(self):
            """Devolver el elemento almacenado en esta Posicion""" 

            self.without_error()

        def __eq__(self, otro):
            """Devuelve  True si otro representa la misma localizacion"""

            self.without_error()
            
        def __ne__(self, otro):
            """Devuelve True si otro no representa la misma localizacion"""

            self.without_error()
        
        def without_error(self): raise NotImplementedError('Debe implementarse para subclase')
        
    #-- metodos abstractos que las subclases concretas deben soportar -----
    def root(self):
        """Devuelve Position que es la raiz del arbol (o None si es vacio)"""

        self.without_error()

    def parent(self, p):
        """Devuelve Position que es el padre de p (o NOne si es vacia)"""
    
        self.without_error()
    
    def num_children(self, p):
        """Devuelve el numero de hijos que Position p tiene"""

        self.without_error()

    def children(self, p):
        """Genera una iteraacion de Positions que represnetan los hijos de p"""
    
        self.without_error()
    
    def __len__(self):
        """Devuelve el numero total de elementos en el arbol"""

        self.without_error()

    def without_error(self):
    
        raise NotImplementedError('Debe implementarse para subclase')   
    #-------- metodos concretos implementados en esta clase -------
    def is_root(self, p):
        """Devuelve True si Position pp es la raiz del arbol"""

        return self.root() == p
    
    def is_leaf(self, p):
        """Devuelve True si Position p no tiene un hijo"""

        return self.num_children(p) == 0
    
    def is_empty(self):
        """Devuelve True si el arbol esta vacio"""

        return len(self) == 0
    
    def depth(self, p):
        """Devuelve el numero de niveles separando posiciones P desde la raiz"""

        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Devuelve la altura del arbol"""

        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Devuelve la altura del subarbol con raiz en la posicion p"""

        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        """Devuelve la altura del subarbol con raiz en lla posicion p
        si p es None, devuelve la altura del arbol entero"""

        if p is None:
            p = self.root()
        
        return self._height2(p)

    def __iter__(self):
        """Genera una iteracion de los elementos del arbol"""

        for p in self.positions():
            yield p.element()
            
    def preorden(self):
        """Genera una iteracio preorden de posiciones en el arbol"""

        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
                
    def _subtree_preorder(self, p):
        """Genera ua iteracion preorden de posiciones en el arbol con raiz de p"""

        yield p
        
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
                
    def positions(self):
        """Genera un iteracion de las posiciones del arbol"""

        return self.preorden()
    
    def postorder(self):
        """Genera una iteracio postorder de posicones en el arbol"""

        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
                
    def _subtree_postorder(self, p):
        """Genera una iteracion postorden de posiciones en el arbol con raiz en p"""

        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
                
        yield p
        
    def breadhfirst(self):
        """Genera una iteracion primero en amplitud de las posciones del arbol"""
        
        from LinkedQueue import LinkedQueue
        
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())

            while not fringe.is_empty():
                p = fringe.dequeue()
                
                yield p
                
                for c in self.children(p):
                    fringe.enqueue(c)
                    
    def inorder(self):
        """Generar una iteracion inorden de posiciones en el arbol"""

        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
                
    def _subtree_inorder(self, p):
        """Genera una iteracion inorden de posiciones en un subarbol etiquetado como p"""

        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
            
        yield p 
        
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
