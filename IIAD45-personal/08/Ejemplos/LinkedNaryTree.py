from NArioTree import NArioTree

class LinkedNAryTree(NArioTree):
    """Representacion enlazada de un arbol n-ario"""

    class _Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent, children):
            self._element = element
            self._parent = parent
            self._children = children

    class Position(NArioTree.Position):
        """Abstraccon que representa la ubicacion de un nodo"""

        def __init__(self, container, node):
            self._container = container
            self._node = node
            
        def element(self):
            """Devuelve el elemento almacenado en esta posicion"""
            return self._node._element

        def __eq__(self, other):
            """Devuelve True sssi representa la misma posicon"""
            return type(other) is type(self) and other._node is self._node
        
    def _validate(self, p):
        """VErifica si la posicon p es valida y devuelve su nodo"""
        if not isinstance(p, self.Position):
            raise TypeError('p debee se de tipo Position')
        if p._container is not self:
            raise ValueError('p no pertenece a este contenedor')
        if p._node._parent is p._node:
            raise ValueError('p ya no es valido')

        return p._node
    
    def _make_position(self, node):
        """'Devuelve una instancia de Position para un nodo"""
        return self.Position(self, node) if node is not None else None
    
    #---------------------------Constructor-----------------------------
    def __init__(self):
        self._root = None
        self._size = 0
    
    #------------------------Metodos de acceso---------------------------
    def __len__(self):
        """Devuelve el numero total de elementos en el arbol"""
        return self._size
    
    def root(self):
        """Devuelve la posicion de la raiz del arbol"""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Devuelve la posicion del padre de p"""
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def children(self, p):
        """Devuelve una lista de las posiciones de los hijos de p"""
        node = self._validate(p)
        return [self._make_position(c) for c in node._children]
    
    def num_children(self, p):
        """Devuelve el numero de hijos de p"""
        node = self._validate(p)
        return len(node._children)
    
    #------------------metodos de modificacion------------------------------
    def _add_root(self, e):
        """Crea la raiz del arbol con el elemento e"""
        if self._root is not None:
            raise ValueError('Raiz ya existe')
        self._root = self._Node(e, parent=None, children=[])
        self._size += 1
        return self._make_position(self._root)

    def add_child(self, p, e):
        """Añade un hijo con elemento e a la posicino p"""
        node = self._validate(p)
        child = self._Node(e, parent=node, children=[])
        node._children.append(child)
        self._size += 1
        return self._make_position(child)

    def _replace(self, p, e):
        """Reemplaza el elemento en la posicion p con e"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    def _delete(self, p):
        """Elimina el nodo en la posicion p y lo reemplaza con su primer hijo si existe."""
        node = self._validate(p)
        if self.num_children(p) > 1:
            raise ValueError('p tiene mas de un hijo')

        child = node._children[0] if node._children else None
        
        if child is not None:
            child._parent = node._parent
            
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            parent._children.remove(node)
            if child is not None:
                parent._children.append(child)

        self._size -= 1
        node._parent = node
        return node._element
    
    def __str__(self):
        """Devuelve una representación visual del árbol n-ario."""
        if self._root is None:
            return "Árbol vacío"

        def _visualizar(p, nivel=0):
            """Función recursiva para generar la estructura del árbol."""
            result = "   " * nivel + str(p.element()) + "\n"
            for hijo in self.children(p):
                result += _visualizar(hijo, nivel + 1)
            return result

        return _visualizar(self.root())

nario = LinkedNAryTree()

padre = nario._add_root(1)
hijo1 = nario.add_child(padre, 2)


print(nario)