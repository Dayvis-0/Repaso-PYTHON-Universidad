# La clase LinkedBinaryTree

from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Representacoin enlazada de una estructura arbol binaria"""

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent = None, left = None, right =None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            
    class Position(BinaryTree.Position):
        """Una abstraccion que representa la ubicacion de un elemento"""

        def __init__(self, container, node):
            self._container = container
            self._node = node
            
        def element(self):
            """Devuelve el elemento almacenado en esta pposicion"""

            return self._node._element

        def __eq__(self, other):
            """Devuelve True si other representa la misma posicion"""

            return type(other) is type(self) and other._node is self._node
        
    def _validate(self, p):
        """Devolver el nodo asociado, si la posicion es valida"""

        if not isinstance(p, self.Position):
            raise TypeError('p debe se de tipo Position')
        if p._container is not self:
            raise ValueError('p no pertenece a este contenedor')
        if p._node._parent is p._node:
            raise ValueError('p ya no es valid')
        
        return p._node
    
    def _make_position(self, node):
        """Devuelve una instancia de Position para un nodo"""

        return self.Position(self, node) if node is not None else None
    
    #------------------------ contructor del arbol binario ----------------------
    def __init__(self):
        self._root = None
        self._size = 0
        
    #-----------------------accesores publicos-------------------
    def __len__(self):
        """Devuelve el numero total de elementos en este arbol"""
        
        return self._size
    
    def root(self):
        """Devuelve la posicion de la raiz del arboll"""

        return self._make_position(self._root)
    
    def parent(self, p):
        """Devuelve la posicion del padre p"""

        node = self._validate(p)

        return self._make_position(node._parent)

    def left(self, p):
        """Devuelve la posicion del izquierdo de p"""

        node = self._validate(p)
        
        return self._make_position(node._left)

    def right(self, p):
        """Devuelve la posicion del derecho p"""

        node = self._validate(p)

        return self._make_position(node._right)

    def num_children(self, p):
        """Devuelve el numero de hijos de la posicion p"""

        node = self._validate(p)
        count = 0
        
        if node._left is not None:
            count += 1
        
        if node._right is not None:
            count += 1
            
        return count
    
    def _add_root(self, e):
        """Pone el elemento e en la raiz del arbol vacio y devuelve la posicion
        Origina VallueError si el arbol no esta vacio"""

        if self._root is not None: raise ValueError('Raiz no existe')

        self._root = self._Node(e)
        self._size = 1
        
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        """Crea un grupo hijo izquierdo para la posicion p
        Origina un ValueError si la posicion p es invalida"""

        node = self._validate(p)

        if node._left is not None: raise ValueError('Hijo izquierdo existe')

        node._left = self._Node(e, node)
        self._size += 1

        return self._make_position(node._left)

    def _add_right(self, p, e):
        """"Crear un nuevo hijo derecho para la posicon p
        Origina un ValueError si la posicion p es invalida"""

        node = self._validate(p)

        if node._right is not None: raise ValueError('Hijo derecho existe')

        self._size += 1
        node._right = self._Node(e, node)

        return self._make_position(node._right)

    def _replace(self, p, e):
        """Reemplaza el elemento en la posicion p con e"""

        node = self._validate(p)
        old = node._element
        node._element = e

        return old
    
    def _delete(self, p):
        """Borra en nodo en la posicion p y lo reemplaza con su hijo
        Devuelve el valor que ha sido almacenado en la posicion p 
        Origina un ValueError si la posicion p es invalida o p tiene dos hijos"""

        node = self._validate(p)

        if self.num_children(p) == 2: raise ValueError('p tiene dos hijos')

        child = node._left if node._left else node._right

        if child is not None:
            child._parent = node._parent
        
        if node is self._root:
            self._root = child
    
        else:
            parent = node._parent

            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        
        self._size -= 1
        node._parent = node
        
        return node._element
    
    def _attach(self, p, t1, t2):
        """Adjunta los arboles t1 y t2 como los hijos izquierdo y derecho de p"""

        node = self._validate(p)

        if not self.is_leaf(p): raise ValueError('Debe ser una hoja')

        if not type(self) is type(t1) is type(t2):
            raise TypeError('Los tipos de arbol deben de coincidir')
        
        self._size += len(t1) + len(t2)
        
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
            
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0    
                    
    def is_balanced(self, p=None):
        """Devuelve True si el arbol es quilibrado, False si no lo es"""
        if p is None:
            p = self.root()

        if p is None:
            return True
        
        left_right = self._height2(self.left(p)) if self.left(p) else 0
        right_height = self._height2(self.right(p)) if self.right(p) else 0
        
        if abs(left_right - right_height) > 1:
            return False
        
        left_balanced = self.is_balanced(self.left(p)) if self.left(p) else True
        right_balanced = self.is_balanced(self.right(p)) if self.right(p) else True

        return left_balanced and right_balanced
        
    def __str__(self):
        """Representación visual del árbol binario"""
        if self._root is None:
            return "<árbol vacío>"
        
        tree_lines = self._build_string_levels()
        return "\n".join(tree_lines)

    def _build_string_levels(self):
        """Construye la representación en niveles del árbol"""
        if self._root is None:
            return []

        from collections import deque

        queue = deque([(self._root, 0)])
        level_dict = {}

        while queue:
            node, depth = queue.popleft()

            if depth not in level_dict:
                level_dict[depth] = []

            level_dict[depth].append(str(node._element) if node else " ")

            if node:
                queue.append((node._left, depth + 1))
                queue.append((node._right, depth + 1))

        max_width = 4  # Ajuste de espaciado
        max_depth = max(level_dict.keys())

        tree_lines = []
        for depth in range(max_depth + 1):
            level_str = " ".join(el.center(max_width) for el in level_dict[depth])
            tree_lines.append(level_str.rstrip())

            if depth < max_depth:
                branches = []
                for i in range(len(level_dict[depth])):
                    left = "/" if 2 * i < len(level_dict[depth + 1]) and level_dict[depth + 1][2 * i] != " " else " "
                    right = "\\" if 2 * i + 1 < len(level_dict[depth + 1]) and level_dict[depth + 1][2 * i + 1] != " " else " "
                    branches.append(left + " " * (max_width - 2) + right)
                tree_lines.append(" ".join(branches).rstrip())

        return tree_lines

lbt = LinkedBinaryTree()
lbt1 = LinkedBinaryTree()
lbt2 = LinkedBinaryTree()

root = lbt._add_root(1)
n2 = lbt._add_left(root, 2)
n1000 = lbt._add_left(root, 100)
n3 = lbt._add_right(root, 3)
n4 = lbt._add_left(n2, 4)
n5 = lbt._add_right(n3,5)
lbt._replace(root, 10)
lbt._replace(n3, 30)
lbt._delete(n4)
lbt._delete(n5)

lbt1._add_root(40)
lbt2._add_root(50)

lbt._attach(n2, lbt1, lbt2)
n40 = lbt.left(n2)
n50 = lbt.right(n2)

print(f'Numero de hijos de {lbt._root._element} es: {lbt.num_children(root)}')

print(f'El hijo derecho de {n2.element()} es : {lbt.right(n2).element()}')
print(f'El hijo izquierdo de {n2.element()} es : {lbt.left(n2).element()}')

print(f'El hijo izquierdo de {n2.element()} es : {lbt.parent(n2).element()}')

print(f'El arbol es: {lbt.root().element()}')

print(lbt)

print('Preorden | padre - hijo izquierdo - hijo derecho ')
for  posi in lbt.preorden():
    print(posi.element(), end=' ')

print('\n\nPostorden | hijo izquierdo - hijo derecho - padre')
for  posi in lbt.postorder():
    print(posi.element(), end=' ')

print('\n\nInorden | hijo izquierddo - padre - hijo derecho')
for  posi in lbt.inorder():
    print(posi.element(), end=' ')

print(f'\n\nProfundidad del arbol | Cantidad de niveles que hay desde la raiz hazta el nodo: {lbt.depth(n40)}')

print(f'\nAltura del arbol | Distancia macimahacia abajo: {lbt.height(root)}')

print('\nAmplitud del arbol | Visita los nodos nivel por nivel')
for c in lbt.breadhfirst():
    print(c.element(), end=' ')
    
print("\nArbol en equilibrio? | Si el subarbol izquierdo y derecho tienen altura similar")
if lbt.is_balanced():
    print('El arbol si esta balanceado')
else:
    print('El arbol no si esta balanceado')