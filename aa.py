from BinaryTree import BinaryTree

class AVLTree(BinaryTree):
    """Representación de un árbol AVL con un árbol binario enlazado"""

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right', '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._height = 0  # Altura inicial del nodo es 0

    class Position(BinaryTree.Position):
        """Una abstracción que representa la ubicación de un elemento"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Devuelve el elemento almacenado en esta posición"""
            return self._node._element

        def __eq__(self, other):
            """Devuelve True si other representa la misma posición"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Devuelve el nodo asociado, si la posición es válida"""
        if not isinstance(p, self.Position):
            raise TypeError('p debe ser de tipo Position')
        if p._container is not self:
            raise ValueError('p no pertenece a este contenedor')
        if p._node._parent is p._node:
            raise ValueError('p ya no es válido')
        return p._node

    def _make_position(self, node):
        """Devuelve una instancia de Position para un nodo"""
        return self.Position(self, node) if node is not None else None

    # ------------------------- Métodos del Árbol AVL ----------------------

    def _update_height(self, node):
        """Actualiza la altura del nodo."""
        if node is None:
            return -1
        left_height = node._left._height if node._left else -1
        right_height = node._right._height if node._right else -1
        node._height = 1 + max(left_height, right_height)
        return node._height

    def _balance_factor(self, node):
        """Devuelve el factor de balance de un nodo (altura subárbol izquierdo - altura subárbol derecho)"""
        left_height = node._left._height if node._left else -1
        right_height = node._right._height if node._right else -1
        return left_height - right_height

    def _rotate_left(self, node):
        """Realiza una rotación a la izquierda."""
        new_root = node._right
        node._right = new_root._left
        if new_root._left:
            new_root._left._parent = node
        new_root._parent = node._parent
        if node._parent is None:
            self._root = new_root
        elif node == node._parent._left:
            node._parent._left = new_root
        else:
            node._parent._right = new_root
        new_root._left = node
        node._parent = new_root

        # Actualizamos las alturas de los nodos involucrados
        self._update_height(node)
        self._update_height(new_root)

    def _rotate_right(self, node):
        """Realiza una rotación a la derecha."""
        new_root = node._left
        node._left = new_root._right
        if new_root._right:
            new_root._right._parent = node
        new_root._parent = node._parent
        if node._parent is None:
            self._root = new_root
        elif node == node._parent._right:
            node._parent._right = new_root
        else:
            node._parent._left = new_root
        new_root._right = node
        node._parent = new_root

        # Actualizamos las alturas de los nodos involucrados
        self._update_height(node)
        self._update_height(new_root)

    def _rebalance(self, node):
        """Realiza rotaciones si el árbol está desequilibrado."""
        while node is not None:
            self._update_height(node)
            balance = self._balance_factor(node)

            if balance > 1:  # Desbalanceo hacia la izquierda
                if self._balance_factor(node._left) < 0:
                    self._rotate_left(node._left)
                self._rotate_right(node)
            elif balance < -1:  # Desbalanceo hacia la derecha
                if self._balance_factor(node._right) > 0:
                    self._rotate_right(node._right)
                self._rotate_left(node)

            node = node._parent

    def _add_root(self, e):
        """Pone el elemento e en la raíz del árbol vacío y devuelve la posición."""
        if self._root is not None:
            raise ValueError('Raíz ya existe')
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Agrega un hijo izquierdo para la posición p"""
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Ya existe un hijo izquierdo')
        node._left = self._Node(e, node)
        self._size += 1
        self._rebalance(node._left)  # Reequilibrar después de la inserción
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Agrega un hijo derecho para la posición p"""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Ya existe un hijo derecho')
        node._right = self._Node(e, node)
        self._size += 1
        self._rebalance(node._right)  # Reequilibrar después de la inserción
        return self._make_position(node._right)

    def _delete(self, p):
        """Elimina el nodo en la posición p y lo reemplaza con su hijo"""
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('El nodo tiene dos hijos')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node == parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        self._rebalance(child)  # Reequilibrar después de la eliminación
        node._parent = node
        return node._element