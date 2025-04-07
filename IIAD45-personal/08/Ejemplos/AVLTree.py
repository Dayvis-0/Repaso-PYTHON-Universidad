from BinaryTree import BinaryTree

class AVLTree(BinaryTree):
    """Representacion de un arbol AVL con un arbol binario enlazado"""

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right', '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._height = 0
            
    class Position(BinaryTree.Position):
        """Una abstraccion que representa la ubiacion de un elemento"""

        def __init__(self, container, node):
            self._container =container
            self._node = node
            
        def element(self):
            """Devuelve el elemento almacendado en esta posicion"""
            return self._node._element
        
        def __eq__(self, otro):
            "Devuelve True si otro representa la misma posicion"
            return type(otro) is type(self) and otro._node is self._node
        
    def _validate(self, p):
        """Devuelve el nodo asociado, si la posicion en valida"""
        if not isinstance(p, self.Position):
            raise TypeError('p debe ser de tipo Position')
        if p._container is not self:
            raise ValueError('p no pertenece a este contendor')
        if p._node._parent is p._node:
            raise ValueError('p ya no es valido')
        return p._node
    
    def _make_position(self, node):
        """Devuelve una instancia de Position par un nodo"""
        return self.Position(self, node) if node is not None else None
    
    def __init__(self):
        self._root = None
        self._size = 0    
    #------------------Metodos de Arbol AVL-------------------------
    def _update_height(self, node):
        """Actualiza la altura del nodo"""
        if node is None:
            return -1
        
        left_height = node._left._height if node._left else -1
        right_height = node._right._height if node._right else -1
        node._height = 1 + max(left_height, right_height)

        return node._height
    
    def _balance_factor(self, node):
        """Devuelve el factor de balance de un nodo (altura suarbol izquierdo
        - altura subarbol derecho)"""
        left_height = node._left._height if node._left else - 1
        right_height = node._right._height if node._right else - 1

        return left_height - right_height
    
    def _rotate_left(self, node):
        """Realiza una rotacion a la izquierda"""
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
        
        self._update_height(node) 
        self._update_height(new_root)

    def _rotate_right(self, node):
        """Realiza una rotacion a la derecha"""
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
        
        self._update_height(node)
        self._update_height(new_root)
        
    def _rebalance(self, node):
        """Realiza rotaciones si el arbol esta desequilibrado"""
        while node is not None:
            self._update_height(node)
            balance = self._balance_factor(node)
            
            if balance > 1:
                if self._balance_factor(node._left) < 0:
                    self._rotate_left(node._left)
                self._rotate_right(node)
            elif balance < -1:
                if self._balance_factor(node._right) > 0:
                    self._rotate_right(node._right)
                self._rotate_left(node)

            node = node._parent
    
    def _add_root(self, e):
        """Pone el elemento e en la raiz del arbol vacio y devuelve la posicion"""
        if self._root is not None:
            raise ValueError('Raiz ya existe')
        self._root = self._Node(e)
        self._size = 1
        
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Agrega un hijo izquieerdo para la posicion p"""
        node = self._validate(p)

        if node._left is not None:
            raise ValueError('Ya equiste un hijo izquierdo')
        
        node._left = self._Node(e, node)
        self._size += 1
        self._rebalance(node._left)

        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Agrega un hijo derecho para la posicion p"""
        node = self._validate(p)
        if node._right is not None: raise ValueError('Ya existe un hijo derecho')

        node._right = self._Node(e, node)
        self._size += 1
        self._rebalance(node._right)

        return self._make_position(node._right)
    
    def _replace(self, p, e):
        """Reemplaza el elemento en la posiiocn p con e"""
        node = self._validate(p)
        old = node._element
        node._element = e
        
        return old

    def _delete(self, p):
        """Elimina el nodo en la posicion p y lo reemplaza con su hijo"""
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
                
        self._size += 1
        self._rebalance(child)
        node._parent = node
        
        return node._element
    
    def __str__(self):
        """Representacion visual del arbol binario AVL"""
        if self._root is None:
            return "<arbol vacio>"

        tree_lines = self._build_string_levels()
        return "\n".join("\t"+  line for line in tree_lines)

    def _build_string_levels(self):
        """Construye la representación visual por niveles del árbol"""
        from collections import deque

        if self._root is None:
            return []

        result = []
        queue = deque([(self._root, 0)])
        current_depth = 0
        current_level = []

        while queue:
            node, depth = queue.popleft()

            if depth != current_depth:
                # Si todo el nivel está vacío, rompemos
                if all(v == " " for v in current_level):
                    break
                result.append(current_level)
                current_level = []
                current_depth = depth

            if node is None:
                current_level.append(" ")
                queue.append((None, depth + 1))
                queue.append((None, depth + 1))
            else:
                current_level.append(str(node._element))
                queue.append((node._left, depth + 1))
                queue.append((node._right, depth + 1))

        if current_level and not all(v == " " for v in current_level):
            result.append(current_level)

        # Convertir a líneas de texto con espaciado bonito
        max_width = 4
        tree_lines = []
        for depth, level in enumerate(result):
            level_str = " ".join(el.center(max_width) for el in level)
            tree_lines.append(level_str.rstrip())

            # Agregar ramas solo si no es la última línea
            if depth < len(result) - 1:
                branches = []
                for i in range(len(level)):
                    left = "/" if 2 * i < len(result[depth + 1]) and result[depth + 1][2 * i] != " " else " "
                    right = "\\" if 2 * i + 1 < len(result[depth + 1]) and result[depth + 1][2 * i + 1] != " " else " "
                    branches.append(left + " " * (max_width - 2) + right)
                tree_lines.append(" ".join(branches).rstrip())

        return tree_lines
        
avl = AVLTree()

padre1 = avl._add_root(1)
hijo1 = avl._add_left(padre1, 2)
hijo2 = avl._add_right(padre1, 3)
print(f'Arbol al inicio: \n{avl}')

avl._replace(hijo1, 20)
print(f'Arbol despues del reemplazo:\n{avl}')

hijo1_dehijo1 = avl._add_left(hijo1, 4)
print(f'Arbol despues de otra insercion: \n{avl}')

hijo1_dehijo2 = avl._add_right(hijo1, 5)
print(f'Arbol despues de otra insercion: \n{avl}')
hijo2_dehijo2 = avl._add_right(hijo1_dehijo2, 6)
print(f'Arbol despues de una simple rotacion:\n{avl}')

hijo1_dehijo11 = avl._add_left(hijo1_dehijo1, 7)
print(f'Arbol despues de una doble rotacion:\n{avl}')