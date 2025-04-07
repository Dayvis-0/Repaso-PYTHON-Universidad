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

        return self._build_string(self._root, '', True)
    
    def _build_string(self, node, prefix, is_tail):
        """Construye una representacion en cadena del arbol de forma recursiva"""

        resullt = prefix + ("└──" if is_tail else "├──") + str(node._element) + "\n" 
        children = [child for child in node._children if child is not None]

        for i, child in enumerate(children):
            is_last = (i== len(children) - 1)
            resullt += self._build_string(child, prefix + ('    ' if is_tail else '|      '), is_last)

        return resullt

nario = LinkedNAryTree()

padre = nario._add_root(1)
hijo1 = nario.add_child(padre, 2)
hijo2 = nario.add_child(padre, 3)
hijo_1_de1 = nario.add_child(hijo1, 4)
hijo3 = nario.add_child(padre, 5)

print(f'El arbol al inicio es \n{nario}')

nario._replace(hijo1, 20)

print(f'El arbol despues de reemplazar es \n{nario}')

nario._delete(hijo3)

print(f'El arbol despues de eliminar es \n{nario}')

print(f'Preorden | padre - hijo izquiero - hijo derecho')
for pre in nario.preorden():
    print(pre.element(), end=' ')

print(f'\n\nPostorden | hijo izquierdo - hijo derecho - padre')
for post in nario.postorder():
    print(post.element(), end=' ')
    
print(f'\n\nInorden | primera mitad de hijos- padre - segunda mitad')
for inord in nario.inorder():
    print(inord.element(), end=' ')
    
print(f'\n\nProfundidad del arbol | Cantidad de niveles que hay desde la raiz haste el nodo: {nario.depth(hijo2)}')

print(f'\nAltura del arbol | La distancia maxima hacia abajo: {nario.height(padre)}')

print(f'\nAmplitud de arbol | Visita los nodos nivel por nivel')
for ampli in nario.bradhfirst():
    print(ampli.element(), end=' ')